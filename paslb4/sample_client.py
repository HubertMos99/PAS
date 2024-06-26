import socket

HOST = '127.0.0.1'
PORT = 65432

# Tworzenie gniazda (socketu) klienta
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = 'Hello, echo server!'
    print(f"Wysyłanie wiadomości: {message}")
    s.sendall(message.encode())  # Wysyłanie wiadomości do serwera echa
    data = s.recv(1024)  # Odbieranie odpowiedzi od serwera echa

print(f"Otrzymano od serwera: {data.decode()}")