import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('127.0.0.1', 8080))

while True:
    try:
        msg, client_address = client.recvfrom(2048)
        decoded_msg = msg.decode('ascii').upper()  # Decode, convert to uppercase
        client.sendto(decoded_msg.encode('ascii'), client_address)  # Encode, send back
    except KeyboardInterrupt:
        break

print('cleaning up')
client.close()