import socket

# Konfiguracja serwera
HOST = '127.0.0.1'
PORT = 65432

def get_ip(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return 'Nie znaleziono adresu IP dla podanej nazwy hosta'

# Tworzenie gniazda (socketu) UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Serwer wyszukiwania adresu IP UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)  # Odbieranie danych od klienta i adresu nadawcy
        hostname = data.decode()
        print(f"Otrzymano od {addr}: {hostname}")

        # Pobranie adresu IP na podstawie nazwy hosta
        ip_address = get_ip(hostname)
        print(f"Odsyłanie adresu IP: {ip_address}")

        # Odesłanie adresu IP z powrotem do klienta
        s.sendto(ip_address.encode(), addr)
