import socket
import os

os.system('clear')

s = socket.socket()
host = input(str("Please enter the hostname of the sender: "))
xhost = str(host)
port = 8080
s.connect((host,port))
os.system('clear')
print("Connected to "+xhost+", waiting for data access relay.. ")

filename = str("data.rex")
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
os.system('clear')
print("Data was recieved successfeully!")
