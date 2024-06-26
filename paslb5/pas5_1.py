import socket

SERVER_IP = '212.182.24.27'
SERVER_PORT = 2912

def main():
    # Tworzenie gniazda (socket) dla połączenia TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, SERVER_PORT))

        # Pętla komunikacyjna
        while True:
            # Pobieranie liczby od użytkownika
            number = input("Podaj liczbę (lub 'exit' aby zakończyć): ")

            if number.lower() == 'exit':
                print("Kończenie połączenia...")
                break

            try:
                # Wysłanie liczby do serwera
                sock.sendall(number.encode())

                # Odbieranie odpowiedzi od serwera
                response = sock.recv(1024).decode()

                # Wyświetlanie odpowiedzi
                print(f"Serwer: {response}")

            except Exception as e:
                print(f"Wystąpił błąd: {e}")
                break


if __name__ == "__main__":
    main()
