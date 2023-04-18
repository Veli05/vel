import socket
import uuid
print ("What's your name?")
name = input ()
print ("Hello, " +name)
hostname = socket.gethostname()
print (hostname)
IPaddress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IPaddress.connect(('77.88.8.8', 80))
print ("IP addres of your pc: " +IPaddress.getsockname()[0])
print ("MAC address of your pc: ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
