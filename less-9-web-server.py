import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog connection

print(f'Listening on {bind_ip}:{bind_port}')


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    print(f'Received {request}')
    client_socket.send('ACK!'.encode())
    client_socket.close()


while True:
    client_sock, address = server.accept()
    print(f'Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock, )  # without comma you'd get a.. TypeError:
    )
    client_handler.start()

# udp server


s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 10000))
while True:
    data, addr = s.recvfrom(max_size)
    resp = "Get off my lawn!"
    s.sendto(resp, addr)

