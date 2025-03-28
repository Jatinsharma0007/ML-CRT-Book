import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.137.132"
port = 5000
complete = (ip_add, port)

msg = input("Enter the message: ")
msg = msg.encode("ascii")
s.sendto(msg, complete)
