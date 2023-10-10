from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ListProperty,StringProperty,ColorProperty

class IconButton(ButtonBehavior,FloatLayout):
	
	color = ColorProperty([1,1,1,1])
	bg_color = ColorProperty([1,1,1,1])
	icon = StringProperty("")
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
