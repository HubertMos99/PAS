import socket

def main():
    # Adres serwera i port
    host = '212.182.24.27'
    port = 2902

    try:
        # Utwórz gniazdo UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while True:
                # Pobierz dane od użytkownika
                num1 = input("Podaj pierwszą liczbę: ")
                operator = input("Podaj operator (+, -, *, /): ")
                num2 = input("Podaj drugą liczbę: ")

                # Sprawdź poprawność danych
                if not num1.isdigit() or not num2.isdigit():
                    print("Proszę wprowadzić poprawne liczby.")
                    continue

                if operator not in ('+', '-', '*', '/'):
                    print("Proszę wprowadzić poprawny operator.")
                    continue

                # Skonstruuj wiadomość
                message = f"{num1} {operator} {num2}"

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