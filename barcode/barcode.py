# pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter

number = "55555555555"
my_code = EAN13(number,writer=ImageWriter())
my_code.save("new_codel")