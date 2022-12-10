import socket

hostname = socket.gethostname()
device = socket.gethostbyname(hostname)

print("Your Device Name is : " + hostname)
print("Your Device IP Address is : " + device)