from PIL import Image
from tkinter.filedialog import *

fl = askopenfilename()

img = Image.open(fl[0])

img.save('out.jpg','JPEG',optimize=True,quality=10)
Image.open('out.jpg')