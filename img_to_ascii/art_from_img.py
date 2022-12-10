import pywhatkit

pywhatkit.image_to_ascii_art("dog.png","myart")
readfile = open("myart.txt","r")
print(readfile.read())
