import pyqrcode

text = "text"
qr_code = pyqrcode.create(text)
qr_code.png("save.png",scale=5)
qr_code.show()