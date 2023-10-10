from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDIcon
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Ellipse
from kivy.properties import ColorProperty, ListProperty, StringProperty, NumericProperty
from kivymd.uix.behaviors import CircularElevationBehavior,CommonElevationBehavior,FakeCircularElevationBehavior,CircularRippleBehavior

from kivy.lang import Builder

from kvdesign import uix_path

from os.path import join
from os import getcwd 

Builder.load_file(join(uix_path,"button", "iconbutton.kv"))
class IconButton(ButtonBehavior,FloatLayout):

	icon        = StringProperty("")
	icon_color  = ColorProperty([1,1,1,1])
	bg_color    = ColorProperty([1,1,1,1])
	bg_el_color = ColorProperty([1,1,1,1])
	fg_el_color = ColorProperty([1,1,1,1])
	radius      = ListProperty([2,2,2,2])
	fg_offset   = ListProperty([0,0])
	bg_offset   = ListProperty([0,0])
	blur_radius = NumericProperty(10)
	space       = NumericProperty(6)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)


