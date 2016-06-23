from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from Tkinter import Tk
from tkFileDialog import askopenfilename
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from popups import Convert
import os
import ntpath
from PIL import Image
from hider import unhide
from kivy.uix.label import Label


class Recover(Screen):
   options = ObjectProperty()
   files = ObjectProperty()
   filename= ObjectProperty()
   img = ObjectProperty()

   def load_files(self):
      here = False
      if os.path.exists('files'):
         here = True
      if here == False:
         os.mkdir('files')
      l = os.listdir('files')
      files = [x for x in l if x.endswith('.png')]
      print(files)
      for f in files:
         file = Pngfile()
         file.boss.append(self)
         file.name.text = f[:-4]
         self.files.add_widget(file)

   def close_option(self):
      anim = Animation(pos_hint = {'top':0}, duration = 0.4)
      anim.start(self.options)
      #self.options.pos_hint = {'top': 0} 

   def open_options(self):
      anim = Animation(pos_hint = {'top':.4}, duration = 0.3)
      anim.start(self.options)

   def open_dialog(self):
      tk = Tk()
      tk.iconbitmap(default= 'icon.ico')
      tk.withdraw()
      file = askopenfilename()
      print(' \n')
      print(file)
      head, name = ntpath.split(file)
      print(head)
      print(name)
      self.options.filepath = head + '/'
      if name[-4:] != '.png':
         print('This is not a png file')
         if name[-4:] =='.jpg':
            print('This is a jpg file')
            print('Conerting to png format')
            n = Image.open(file)
            filename = head + '/'+name[:-4] + '.png'
            print(filename)
            k = n.save(filename, 'PNG')
            os.remove(file)
            self.filename.text = name[:-4]
            self.img.source = filename
            self.open_options()
         return
      self.filename.text = name[:-4]
      self.img.source = file
      self.open_options()

   def convert(self):
      print(self.options.filepath)
      file = self.options.filepath + self.filename.text + '.png'
      print(file)
      p = Convert()
      p.open()
      unhide(file)
      print('Recovered hidden file')
      p.status.text = 'Done'
      p.progress.clear_widgets()
      p.progress.add_widget(Label(font_size= '28dp', text='Recovered File Sucessfully', size_hint=(1,1)))
      self.delete()	  
	  
   def refresh(self):
      self.files.clear_widgets()
      self.close_option()
      self.load_files()
      return

   def delete(self):
      name = self.filename.text
      path = self.options.filepath
      file = path + name + '.png'
      print(file)
      os.remove(str(file))
      self.refresh()
      

   def open_folder(self):
      os.startfile('files')



class ROptions(GridLayout):
   filepath = ''

class Pngfile(Button):
   name = ObjectProperty()
   boss = []
   name = ObjectProperty()
   def show_options(self):
      self.boss[0].filename.text = self.name.text
      self.boss[0].img.source = r"icons/Lenna.png"
      print(self.name.text)
      self.boss[0].options.filepath = 'files/'
      self.boss[0].open_options()
      print('called open')
