from kivy.uix.screenmanager import Screen
from Tkinter import Tk
from tkFileDialog import askopenfilename
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from popups import Convert
from hider import hide
import ntpath
import os
from kivy.uix.label import Label

class HidePage(Screen):
   options = ObjectProperty()
   files = ObjectProperty()
   filename= ObjectProperty()

   def load_files(self):
      here = False
      if os.path.exists('files'):
         here = True
      if here == False:
         os.mkdir('files')
      l = os.listdir('files')
      files = [x for x in l if x.endswith('.docx')]
      print(files)
      for f in files:
         file = Wordfile()
         file.boss.append(self)
         file.name.text = f[:-5]
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
      if name[-5:] != '.docx':
         print('This is not an msword file')
         return
      self.filename.text = name[:-5]
      self.open_options()

   def convert(self):
      print(self.options.filepath)
      file = self.options.filepath + self.filename.text + '.docx'
      print(file)
      p = Convert()
      p.open()
	  #Now hiding the file
      hide(file)
      p.progress.clear_widgets()	  
      p.progress.add_widget(Label(font_size= '28dp',size_hint=(1,1),text='File Hidden Successfully'))
      p.status.text = 'Done'
      os.remove(file)
      self.refresh()
	  
   def refresh(self):
      self.files.clear_widgets()
      self.close_option()
      self.load_files()
      return

   def delete(self):
      name = self.filename.text
      path = self.options.filepath
      file = path + name + '.docx'
      print(file)
      os.remove(str(file))
      self.refresh()
      

   def open_folder(self):
      os.startfile('files')


class Wordfile(Button):
   #boss = ObjectProperty()
   boss = []
   name = ObjectProperty()
   def show_options(self):
      self.boss[0].filename.text = self.name.text
      self.boss[0].options.filepath = 'files/'
      self.boss[0].open_options()

class Options(GridLayout):
   filepath = ''