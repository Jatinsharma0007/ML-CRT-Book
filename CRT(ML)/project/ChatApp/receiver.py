import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.137.132"
port = 5000
complete = (ip_add, port)
s.bind(complete)
print("Receiver is up and running")

while True:
    msg, ip_add = s.recvfrom(1024)
    msg=msg.decode("ascii")
    print(msg)
