import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5006
BUFFER_SIZE = 1024


def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        udp_sock.bind((UDP_IP, UDP_PORT))
        print(f"Serwer UDP nasłuchuje na porcie {UDP_PORT}...")

        while True:
            data, addr = udp_sock.recvfrom(BUFFER_SIZE)
            udp_sock.sendto(data, addr)  # Echo the data back to the client


if __name__ == "__main__":
    udp_server()
