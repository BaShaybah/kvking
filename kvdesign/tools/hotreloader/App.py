__author__ = "Khalid Babiker"

from kivy.app import App as Base

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.logger import Logger
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.clock import Clock, mainthread
from kivy.properties import StringProperty, ListProperty

import os
from os.path import join
import sys
import importlib

from .errorscreen import ErrorScreen

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent


class App(Base):

	CLASSES = ListProperty([])
	supported_files = ListProperty(["py", "kv"])
	_workingdir = ListProperty([])
	main_folder = StringProperty("")	
	KVROOT = StringProperty("")
	_KVROOT = StringProperty("")
	kvtitle = StringProperty("")
	init_argv = sys.argv

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self._KVROOT    = join(os.getcwd(), self.main_folder, self.KVROOT)
		
	
	def build(self):
		self.kvtitle = str(os.getcwd()).split(os.path.sep)[-1]
		self.approot    = None
		self.root       = Factory.RelativeLayout()
		
		return super().build()
	
	def on_start(self):
		Window.bind(on_keyboard=self.keys_down)
		
		self.get_all_paths()
		self.start_watchdog()
		
		self.hot_start()
		return super().on_start()
	
	def start_watchdog(self):
		try:
			self.event_handler = FileSystemEventHandler()
			self.observer = Observer()
			self.event_handler.dispatch = self.getcheck
			
			for i in self._workingdir:
				self.observer.schedule(self.event_handler, i, recursive=True)
			
			self.observer.start()	
			Clock.schedule_interval(self.getcheck,1)
			
		except Exception as e:
			self.error_view(e)
			
	def get_all_paths(self):
		for path, dir, lfile in os.walk(join(os.getcwd(), self.main_folder)) :
				for mfile in lfile:
					file = join(path, mfile)
					if file.endswith(".py") or file.endswith(".kv") :
						self._workingdir.append(file)
		return self._workingdir
			
	@mainthread
	def getcheck(self, event):
		if not isinstance(event, FileModifiedEvent):
			return
			
		kfile = event.src_path
		if kfile != self._KVROOT:
			self.app_reloader(kfile)
		else:
			self.rebuild()
					
	def hot_start(self):
		try:
			for file in self._workingdir:
				if file.endswith(".py"):
					imp = str(file).split(str(self.kvtitle))[1].replace(os.path.sep, ".")
					imp = imp.lstrip(".").rstrip(".py")
						
					for cls in self.CLASSES:		
						if cls.lower() == imp.split(".")[-1]:
							exec(f"import {imp}")
							importlib.reload(eval(f"{imp}"))
							exec(f"from {self.main_folder}.{cls.lower()}.{cls.lower()} import {cls}")

				elif file.endswith(".kv") and file != self._KVROOT:
					Builder.load_file(file)

			self.rebuild()
			Logger.info(f"{self.kvtitle}: app start")	

		except Exception as e:
			self.error_view(e)


	def app_reloader(self, file):
		if file is None:
			return
		try:
			if file.endswith(".py"):
				imp = str(file).split(str(self.kvtitle))[1].replace(os.path.sep, ".")
				imp = imp.lstrip(".").rstrip(".py")
				for cls in self.CLASSES:		
					if cls.lower() == imp.split(".")[-1]:

						exec(f"import {imp}")
						importlib.reload(eval(f"{imp}"))
						exec(f"from {self.main_folder}.{cls.lower()}.{cls.lower()} import {cls}")

						Factory.unregister(f"{cls}")
						Factory.register(f"{cls}", eval(f"{cls}"))

			elif file.endswith(".kv") and file != self._KVROOT:
				Builder.unload_file(file)
				Builder.load_file(file)
	
			self.rebuild()
			
		except Exception as e:
			self.error_view(e)
		

	def error_view(self, txt = ""):
		Logger.error(txt)
		
		self.root.clear_widgets()
		self.root.add_widget(ErrorScreen(text=str(txt)))


	def rebuild(self, *args):
		try:
			Builder.unload_file(self._KVROOT)
			self.approot = Builder.load_file(self._KVROOT)

			self.root.clear_widgets()
			self.root.add_widget(self.approot)
			Logger.info(f"{self.kvtitle} : app reloaded")
			
		except Exception as e:
			self.error_view(e)



	def keys_down(self, *args):
		if args[1] == 286:
			self._restarting()	


	def _restarting(self):
		_has_execv = sys.platform != "win32"
		cmd = [sys.executable] + self.init_argv
		if not _has_execv:
			import subprocess

			subprocess.Popen(cmd)
			sys.exit(0)
		else:
			try:
				os.execv(sys.executable, cmd)
			except OSError:
				os.spawnv(os.P_NOWAIT, sys.executable, cmd)
				os._exit(0)

	


		






		
		
		
		
		
		
