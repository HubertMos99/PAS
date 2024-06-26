import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

# Tworzenie gniazda (socketu)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Serwer nasłuchuje na {HOST}:{PORT}")

    # Obsługa jednego klienta
    conn, addr = s.accept()  # Zaakceptowanie połączenia
    with conn:
        print(f"Połączono z {addr}")
        while True:
            data = conn.recv(1024)  # Odczytanie danych od klienta
            if not data:
                break
            message = data.decode()  # Dekodowanie odebranej wiadomości
            print(f"Otrzymano wiadomość: {message}")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn.sendall(current_time.encode())  # Odesłanie bieżącej daty i czasu

        print("Połączenie zakończone")