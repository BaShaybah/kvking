from kivy.properties import ColorProperty, ListProperty, StringProperty, NumericProperty

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kvdesign import uix_path

from os.path import join
from os import getcwd 

Builder.load_file(join(uix_path,"pycompiler", "pycompiler.kv"))
class PyCompiler(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


