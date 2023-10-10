from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import NumericProperty,ColorProperty


from kvdesign.uix.slider import UISlider
from kvdesign.uix.button import IconButton

from kivy.core.audio import SoundLoader
class UIAudioPlayer(MDFloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		#su = SoundLoader().load("assets/aud/kivymd.mp3")
		#su.play()
		#su.seek(30)
