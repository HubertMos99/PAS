import socket

HOST = '127.0.0.1'
PORT = 2910

def handle_client_message(message):
    s = len(message.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        parts = message.split(";")
        if parts[0] == "zad14odp" and parts[1] == "src" and parts[3] == "dst" and parts[5] == "data":
            try:
                src_port = int(parts[2])
                dst_port = int(parts[4])
                data = parts[6]
            except:
                return "BAD_SYNTAX:"
            if src_port == 60788 and dst_port == 2901 and data == "programming in python is fun":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"


# Tworzenie gniazda (socketu) UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)  # Odbieranie danych od klienta
        message = data.decode()
        print(f"Otrzymano od {addr}: {message}")

        # Obsługa wiadomości od klienta
        response = handle_client_message(message)

        # Odsyłanie odpowiedzi do klienta
        s.sendto(response.encode(), addr)
