import socket

def main():
    # Adres serwera i port
    host = '212.182.24.27'
    port = 2900

    # Wiadomość do wysłania
    message = "Hello, server! This is a test message."

    try:
        # Utwórz gniazdo TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Połącz się z serwerem
            s.connect((host, port))

            # Wyślij wiadomość do serwera
            s.sendall(message.encode())

            # Odbierz odpowiedź od serwera
            data = s.recv(1024)

            # Wyświetl otrzymaną odpowiedź
            print(f'Otrzymano odpowiedź od serwera: {data.decode()}')

    except socket.error as err:
        print(f'Błąd podczas połączenia: {err}')


if __name__ == "__main__":
    main()