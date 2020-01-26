import os
import time
import socket
import platform

OSname = str(platform.system())

if OSname == "Windows":

	def clear():

		import os
		os.system('cls')
else:

	def clear():

		import os
		os.system('clear')

clear()

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
xhost = str(host)
print("["+xhost+"]: Waiting for incoming connections..")
conn, addr = s.accept()
clear()
print(addr, "Has connected! Press [ANY-KEY] to send data..")
input(" ")
filename = str("data.rex")
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
clear()
print("Data has been transmitted!")
