# Clock
# .000 As found on line, timer with 1s increment
# .100 Added stop button, properties to change button text




from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime


class MyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__()
        self.zero = None

    def start(self, *varargs):                          # set up the clock, started on button's on_press() event
        self.button1.text = "Clock is running"
        self.button2.text = "Click to stop the clock"
        self.zero = datetime.now()
        event = Clock.schedule_interval(self.on_timeout, 1)     # sets up an on_timeout() event every 1s, fires once

    def on_timeout(self, *args):                        # fires every 1s, updates the clock display
        d = datetime.now() - self.zero
        self.label1.text = datetime.utcfromtimestamp(d.total_seconds()).strftime("%H.%M.%S")

    def stop(self):
        Clock.unschedule(self.on_timeout)
        self.button1.text = "Click to start the clock"
        self.button2.text = "Clock is stopped"


class MainApp(App):
    def build(self):
        return MyApp()


if __name__ == '__main__':
    MainApp().run()
