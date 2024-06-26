import socket
import random

HOST = '127.0.0.1'
PORT = 2912

def main():
    # Tworzenie gniazda (socket) dla połączenia TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # Wiązanie gniazda z adresem i portem
        server_sock.bind((HOST, PORT))
        # Nasłuchiwanie na połączenia przychodzące
        server_sock.listen(1)
        print(f"Serwer nasłuchuje na porcie {PORT}...")

        # Akceptowanie połączenia od klienta
        conn, addr = server_sock.accept()
        with conn:
            print(f"Połączono z {addr}")

            # Losowanie liczby
            target_number = random.randint(1, 100)
            print(f"Wylosowana liczba: {target_number}")

            while True:
                try:
                    # Odbieranie liczby od klienta
                    data = conn.recv(1024)
                    if not data:
                        break
                    number_str = data.decode()
                    print(f"Otrzymano liczbę: {number_str}")

                    # Sprawdzanie, czy liczba jest równa, większa czy mniejsza od wylosowanej liczby
                    try:
                        number = int(number_str)
                        if number < target_number:
                            response = "Twoja liczba jest za mała."
                        elif number > target_number:
                            response = "Twoja liczba jest za duża."
                        else:
                            response = "Gratulacje! Odgadłeś liczbę."
                            conn.sendall(response.encode())
                            break  # Zamknięcie połączenia po odgadnięciu liczby
                    except ValueError:
                        response = "Proszę podać poprawną liczbę."

                    # Wysyłanie odpowiedzi do klienta
                    conn.sendall(response.encode())

                except Exception as e:
                    print(f"Wystąpił błąd: {e}")
                    break


if __name__ == "__main__":
    main()
