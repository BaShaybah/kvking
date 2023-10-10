from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty,BooleanProperty

from kivy.core.window import Window
class Slide(BoxLayout):
	text = StringProperty("")
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	