import socket

HOST = '127.0.0.1'
PORT = 65432

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return 'Nie znaleziono nazwy dla podanego adresu IP'

# Tworzenie gniazda (socketu) UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Serwer hostnamu UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)  # Odbieranie danych od klienta i adresu nadawcy
        ip_address = data.decode()
        print(f"Otrzymano od {addr}: {ip_address}")

        # Pobranie nazwy hosta na podstawie adresu IP
        hostname = get_hostname(ip_address)
        print(f"Odsyłanie hostnamu: {hostname}")

        # Odesłanie nazwy hosta z powrotem do klienta
        s.sendto(hostname.encode(), addr)
