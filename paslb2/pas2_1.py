import socket

def pobierz_date_i_czas(serwer, port):
    try:
        # Utworzenie gniazda TCP
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Ustawienie timeout na 10 sekund
        gniazdo.settimeout(10)

        # Połączenie z serwerem
        print(f"Łączenie z serwerem {serwer} na porcie {port}...")
        gniazdo.connect((serwer, port))

        # Pobranie danych z serwera
        dane = gniazdo.recv(1024).decode('utf-8')

        # Zamykanie gniazda
        gniazdo.close()

        return dane
    except socket.error as err:
        return f"Nie udało się połączyć z serwerem: {err}"

def main():
    serwer = 'ntp.task.gda.pl'
    port = 13

    # Pobranie i wyświetlenie daty i czasu
    data_czas = pobierz_date_i_czas(serwer, port)
    print(f"Data i czas z serwera {serwer}: {data_czas}")


if __name__ == "__main__":
    main()