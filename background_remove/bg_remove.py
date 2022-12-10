from rembg import remove

from PIL import Image

output_path = "output.png"
input = Image.open('dog.png')

output = remove(input)
output.save(output_path)