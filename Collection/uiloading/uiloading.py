from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty,NumericProperty,ColorProperty
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.animation import Animation


class UILoading(ModalView):
	
	sizell   = ListProperty([100,100])
	color    = ColorProperty([1,1,1,1])
	angel_st = NumericProperty(0)
	angel_en = NumericProperty(360)
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		
		
	def on_open(self):
		""
		Clock.schedule_once(self.cirlo,0)
		Clock.schedule_interval(self.cirlo,.8)
		
	def on_dismiss(self):
		""
		Clock.unschedule(self.cirlo)
		anim = Animation(sizell=[350,350],color=[1,1,1,0], d=0.5)
		
		anim.start(self)
		
	def cirlo(self, *args):
		anim = Animation(sizell=[150,150],color=[1,1,1,1], d=0.35)
		anim += Animation(sizell=[100,100], d=0.35)
		anim.start(self)
		
