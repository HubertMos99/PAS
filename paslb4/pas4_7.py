import socket

HOST = '212.182.24.27'
PORT = 2900
MAX_LENGTH = 20

# Wiadomość do wysłania
message_to_send = "Hello, server!"

# Tworzenie gniazda (socketu) klienta TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Wysyłanie wiadomości
    s.sendall(message_to_send.encode())

    # Odbieranie odpowiedzi
    data = s.recv(MAX_LENGTH).decode()

print(f"Odebrano od serwera: {data}")