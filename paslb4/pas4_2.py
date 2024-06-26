import socket

HOST = '127.0.0.1'
PORT = 65432

# Tworzenie gniazda (socketu)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Serwer echa nasłuchuje na {HOST}:{PORT}")

    # Obsługa jednego klienta
    conn, addr = s.accept()  # Zaakceptowanie połączenia
    with conn:
        print(f"Połączono z {addr}")
        while True:
            data = conn.recv(1024)  # Odczytanie danych od klienta
            if not data:
                break
            print(f"Otrzymano od klienta: {data.decode()}")

            # Odesłanie odebranej wiadomości z powrotem do klienta
            conn.sendall(data)

        print("Połączenie zakończone")
