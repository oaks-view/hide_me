import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import  ScreenManager, Screen, SwapTransition
from kivy.lang import Builder
from myne import iconfonts

from hidepage import HidePage
Builder.load_file('hidepage.kv')
from recover import Recover, ROptions, Pngfile
Builder.load_file('recover.kv')
from popups import Convert
Builder.load_file('popups.kv')

class Home(Screen):
   pass

class Page(Button): #THESE ARE THE BUTTONS ON HOME SCREEN
   pass

class Manager(ScreenManager):
   pass


class HideApp(App):
   def build(self):
      m = Manager()
      return m
   def on_start(self):
      self.root.transition = SwapTransition()

if __name__ == "__main__":
   Window.fullscreen = False
   print('STARTED APP NOW')
   iconfonts.register('default_fonts','ionicons.ttf','ionicons.fontd')
   HideApp().run()