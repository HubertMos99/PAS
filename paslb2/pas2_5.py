import socket

def main():
    # Adres serwera i port
    host = '212.182.24.27'
    port = 2901

    try:
        # Utwórz gniazdo UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while True:
                # Wczytaj wiadomość od użytkownika
                message = input("Wpisz wiadomość (wpisz 'q' aby zakończyć): ")

                # Jeśli użytkownik wpisze 'q', wyjdź z pętli
                if message.lower() == 'q':
                    print("Zakończono komunikację.")
                    break

                # Wyślij wiadomość do serwera
                s.sendto(message.encode(), (host, port))

                # Odbierz odpowiedź od serwera
                try:
                    data, addr = s.recvfrom(1024)
                    print(f'Otrzymano odpowiedź od serwera: {data.decode()}')
                except socket.timeout:
                    print("Brak odpowiedzi od serwera.")

    except socket.error as err:
        print(f'Błąd podczas połączenia: {err}')


if __name__ == "__main__":
    main()