from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import NumericProperty,ColorProperty


from kivy.lang import Builder
from kvdesign import uix_path
from os.path import join

Builder.load_file(join(uix_path,"slider", "slider.kv"))

class UISlider(MDFloatLayout):

	forward  = ColorProperty([0.2,0.4,0.6,0.8])
	cir  = ColorProperty([1,1,0,1])
	backward = ColorProperty([0,0,0,0.5])

	value    = NumericProperty(100)
	max      = NumericProperty(100)
	horz     = NumericProperty(10)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)


	def on_touch_down(self, touch):
		if self.collide_point(touch.x,touch.y):
			touch.grab(self)
			self.value = int(self.max * ((touch.x - self.x)/self.width))

		return super().on_touch_down(touch)
	
	def on_touch_move(self, touch):
		if touch.grab_current is self and touch.x > self.x and touch.x < self.right:
			self.value = int(self.max * ((touch.x - self.x)/self.width))

		return super().on_touch_move(touch)
	
	def on_touch_up(self, touch):
		touch.ungrab(self)
		return super().on_touch_up(touch)
		
