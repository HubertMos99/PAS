import socket


def main():
    # Adres serwera i port
    host = '212.182.24.27'
    port = 2901

    # Wiadomość do wysłania
    message = "Witam, witam."

    try:
        # Utwórz gniazdo UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Wyślij wiadomość do serwera
            s.sendto(message.encode(), (host, port))

            # Odbierz odpowiedź od serwera
            data, addr = s.recvfrom(1024)

            # Wyświetl otrzymaną odpowiedź
            print(f'Otrzymano odpowiedź od serwera: {data.decode()}')

    except socket.error as err:
        print(f'Błąd podczas połączenia: {err}')


if __name__ == "__main__":
    main()