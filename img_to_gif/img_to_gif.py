import imageio

img_name = ["1.png","2.png"]

imgage = []

for img in img_name:
    imgage.append(imageio.imread(img))

imageio.mimsave('export.gif',img,'GIF',duration=1)

