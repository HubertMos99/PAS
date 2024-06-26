import socket

# Konfiguracja serwera
HOST = '127.0.0.1'
PORT = 65432

# Tworzenie gniazda (socketu) UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Serwer echa UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)  # Odbieranie danych od klienta i adresu nadawcy
        print(f"Otrzymano od {addr}: {data.decode()}")

        # Odesłanie odebranej wiadomości z powrotem do klienta
        s.sendto(data, addr)
        print(f"Odesłano do {addr}: {data.decode()}")
