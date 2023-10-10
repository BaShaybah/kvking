from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty,StringProperty,ListProperty
from kivy.animation import Animation

class NavDrawer(FloatLayout):
	
	active = BooleanProperty(False)
	filepath = StringProperty("")
	select = StringProperty([])
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.register_event_type("on_open")
		self.register_event_type("on_dismiss")
		
	def on_touch_down(self,touch):
		self.st1 = touch.x
		self.sy1 = touch.y
		if not self.collide_point(touch.x,touch.y) and self.active:
			self.dismiss()
		return super().on_touch_down(touch)
	
	def on_touch_move(self,touch):
		self.st2 = touch.x
		self.sy2 = touch.y
		if self.st2 - self.st1 > 160 and max([self.sy1,self.sy2]) - min([self.sy1,self.sy2]) <= 100:
			#self.x = 0
			self.open()
		return super().on_touch_move(touch)
	
	def on_touch_up(self,touch):
		return super().on_touch_up(touch)
		
	def open(self):
		""" __init__ """
		anim = Animation(x=0,d=0.2).start(self)
		self.active = True
		self.dispatch("on_open")
			
	def dismiss(self):
		""" __init__ """
		self.active = False
		sx = 0-self.width
		anim = Animation(x=sx,d=0.2).start(self)
		self.dispatch("on_dismiss")
		
	def on_open(self):
		""" __init__ """
		
	def on_dismiss(self):
		""" __init__ """