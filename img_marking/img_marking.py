from PIL import Image ,ImageDraw, ImageFont

img = Image.open("dog.png")
draw = ImageDraw.Draw(img)
text = "Dog"
font = ImageFont.truetype("are.ttf",120)
textwidth, textheight = draw.textsize(text,font)
w,h = img.size
x = w / 2 - textwidth / 2
y = h / 2 - textheight / -50

draw.text((x,y),text, font=font)
img.save(r'export.png')