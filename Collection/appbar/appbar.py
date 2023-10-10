from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty,StringProperty

class AppBar(FloatLayout):
    
    action_items = ListProperty([])
    title = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)