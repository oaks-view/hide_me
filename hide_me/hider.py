from PIL import Image
import stepic


def hide(doc):
   file = open(doc,'rb')
   data = file.read()
   img = Image.open(r"icons/Lenna.png")
   img2 = stepic.encode(img, data)
   pic = doc[:-5] + '.png'
   img2.save(pic,'PNG')
   print('done saving data in image...')
   file.close()
   return


def unhide(pic):
   img = Image.open(pic)
   doc = pic[:-4] + '.docx'
   file = open(doc,'wb')
   d = stepic.decode(img)
   #info = d.decode()
   file.write(d)
   file.close()
   return
