from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import NumericProperty,ColorProperty, StringProperty, BooleanProperty, ColorProperty
from kivy.animation import Animation
from kivy.clock import Clock

class UISwitch(MDFloatLayout):

    text_on  = StringProperty("fff")
    text_off = StringProperty("fff")

    bg_on    = ColorProperty([0.2, 0.4, 0.8, 0.8])
    bg_off   = ColorProperty([0.8, 0.4, 0.2, 0.8])

    active     = BooleanProperty(True)
    _curso     = NumericProperty(0)
	
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_create")
        Clock.schedule_once(self.set_style)

    def on_create(self):
        """ """

    def set_style(self, *args):
        if self.active:
            self.text_on  = "fff"
            self.text_off = "000"
            self._curso = self.width - self.ids.tog.width - 15
            self.bg_on    = [0.2, 0.4, 0.8, 0.8]
            self.bg_off   = [0.8, 0.4, 0.2, 0.0]
            #self.ids.tog.x = self.right - self.ids.tog.width - 15

        elif not self.active:
            self.text_off  = "fff"
            self.text_on = "000"
            self._curso = 15
            self.bg_on    = [0.2, 0.4, 0.8, 0.0]
            self.bg_off   = [0.8, 0.4, 0.2, 0.8]
            #self.ids.tog.x = self.x +  15

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            touch.grab(self)
            if self.active:
                self.active = False
                
                anima = Animation(
                    _curso= 15,
                    bg_on=[0,0,0,0],
                    bg_off=[0.8, 0.4, 0.2, 0.8],
                    d=0.2)
                anima.start(self)

                self.text_on = "000"
                self.text_off = "fff"

            elif not self.active:
                self.active = True
                
                anima = Animation(
                    _curso = self.width - self.ids.tog.width - 15,
                    bg_off=[0,0,0,0],
                    bg_on=[0.2, 0.4, 0.8, 0.8],
                    d=0.2)
                anima.start(self)

                self.text_on = "fff"
                self.text_off = "000"

        return super().on_touch_down(touch)
    
    def on_touch_move(self, touch):
        return super().on_touch_move(touch)
    
    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
        return super().on_touch_up(touch)

