import socket
import time

def send_ping_to_udp_ports(ip, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
            udp_sock.sendto(b'PING', (ip, port))
            try:
                udp_sock.settimeout(1)
                data, _ = udp_sock.recvfrom(1024)
                if data == b'PONG':
                    print(f"Port {port} jest częścią sekwencji.")
                    yield port
            except socket.timeout:
                pass


def main():
    # Adres IP serwera
    SERVER_IP = '212.182.24.27'
    # Port TCP docelowy
    SERVER_TCP_PORT = 2913

    # Wygenerowanie listy portów UDP kończących się na 666 (np. 666, 1666, 2666, ..., 65666)
    udp_ports = [port for port in range(666, 65667, 1000)]

    # Znalezienie portów UDP należących do sekwencji otwierającej
    valid_udp_ports = list(send_ping_to_udp_ports(SERVER_IP, udp_ports))

    if not valid_udp_ports:
        print("Nie znaleziono żadnych portów UDP w sekwencji.")
        return

    print("Wysłanie sekwencji otwierającej port TCP...")

    # Wysłanie sekwencji otwierającej
    for port in valid_udp_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
            udp_sock.sendto(b'PING', (SERVER_IP, port))
            time.sleep(1)  # Przerwa między wysyłaniem

    print("Próba połączenia z ukrytą usługą na porcie TCP...")

    # Próba połączenia z ukrytą usługą na porcie TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        try:
            tcp_sock.connect((SERVER_IP, SERVER_TCP_PORT))
            message = tcp_sock.recv(1024).decode()
            print(f"Odpowiedź od serwera: {message}")
        except Exception as e:
            print(f"Nie udało się połączyć z ukrytą usługą: {e}")


if __name__ == "__main__":
    main()
