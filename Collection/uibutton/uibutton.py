from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ColorProperty
from kivy.uix.behaviors import ButtonBehavior

class UIButton(ButtonBehavior,FloatLayout):
	
	icon = StringProperty("")
	text = StringProperty("")
	
	icon_color = ColorProperty([0.2,0.4,0.8,1])
	text_color = ColorProperty([0,0,0,1])

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	