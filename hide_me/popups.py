from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty
from kivy.animation import Animation


class Convert(ModalView):
   loading= ObjectProperty()
   progress = ObjectProperty()
   status = ObjectProperty()
   def load(self):
      anim = Animation(p = 360, duration= 1) + Animation(p=60, duration=0)
      anim.repeat = True
      anim.start(self.loading)