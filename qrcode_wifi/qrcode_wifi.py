import wifi_qrcode_generator as qr
from PIL import Image

img = qr.wifi_qrcode("demo",False,"WPA","123456789")
img.save("output.jpg","JPEG")



