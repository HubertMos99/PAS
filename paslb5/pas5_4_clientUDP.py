import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 5006
BUFFER_SIZE = 1024
MESSAGE = b'Hello, UDP!'


def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        start_time = time.time()
        udp_sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        data, addr = udp_sock.recvfrom(BUFFER_SIZE)
        end_time = time.time()

        print(f"Otrzymano: {data.decode()}")
        print(f"Czas przesyłu pakietu UDP: {end_time - start_time} sekund")


if __name__ == "__main__":
    udp_client()
