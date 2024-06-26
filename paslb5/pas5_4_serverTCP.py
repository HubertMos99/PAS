import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.bind((TCP_IP, TCP_PORT))
        tcp_sock.listen(1)
        print(f"Serwer TCP nasłuchuje na porcie {TCP_PORT}...")

        conn, addr = tcp_sock.accept()
        with conn:
            print(f"Połączono z {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(data)


if __name__ == "__main__":
    tcp_server()
