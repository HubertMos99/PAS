import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b'Hello, TCP!'


def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.connect((TCP_IP, TCP_PORT))

        start_time = time.time()
        tcp_sock.sendall(MESSAGE)
        data = tcp_sock.recv(BUFFER_SIZE)
        end_time = time.time()

        print(f"Otrzymano: {data.decode()}")
        print(f"Czas przesyłu pakietu TCP: {end_time - start_time} sekund")


if __name__ == "__main__":
    tcp_client()
