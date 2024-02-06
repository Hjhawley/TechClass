import socket

# AF_INET is the family or network, SOCK_DGRAM is a datagram for UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_string = input("Enter a string to send: ")
server.sendto(my_string.encode('ascii'), ('127.0.0.1', 8080))
# '127.0.0.1' is the 'localhost' or 'loopback' address

msg, server_address = server.recvfrom(2048)
print(msg)

server.close()