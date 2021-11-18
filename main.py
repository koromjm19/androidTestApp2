import kivy
from kivy.app import App #main app class, creates window and graphics
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MainWindow(Screen):
    def clear(self):
        self.password.text = ""
    def btn(self):
        show_popup()

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("multiscreen.kv")

class P(FloatLayout):
    pass

class multiScreenApp(App):
    def build(self):
        return kv

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint = (None,None), size=(400,400))
    popupWindow.open()

if __name__ == "__main__":
    multiScreenApp().run()