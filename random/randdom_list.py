import random
import time
import sys, os

name_list = [
    "นายสมตุ่ย ลุยทุ่งกระเจียว",
    "นายสมศรี",
    "นายสมเหยา",
    "นางสมหญิง ทิงเกอร์เบล",
    "บักเดิพ",
    "บักหยอย"
]
for i in range(5):
    print("กำลังเริ่มสุ่มรายชื่อ ",5-i)
    time.sleep(1)
    
allname = []
for i in range(3):
    congrad = random.choice(name_list)
    allname.append(congrad)
    #name_list.remove(congrad)
    
print("=================")
print("รายชื่อผู้ที่โชคดีได้แก่")
print("=================")

for nm in allname:
    print("{}".format(nm))
    print('-----------------')