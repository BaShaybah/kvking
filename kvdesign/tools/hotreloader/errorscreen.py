from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_string("""
<ErrorScreen>:
    id:src
    text:""
    canvas.before:
        Color:
            rgba:1,1,1,1
        Rectangle:
            pos:self.pos
            size:self.size
            
    BoxLayout:
        ScrollView:
            effect_cls:"ScrollEffect"
            BoxLayout:
                padding:"10dp"
                size_hint:None,None
                size: self.minimum_size
                
                Label:
                    id:lbl
                    halign:"left"
                    color:1,0,0,1
                    text:src.text
                    size_hint:None,None
                    size:self.texture_size

""")

class ErrorScreen(BoxLayout):
	
	text = StringProperty("")
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)