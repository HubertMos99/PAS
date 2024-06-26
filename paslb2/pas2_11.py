import socket
import sys

def polacz_sie_z_serwerem_i_wyslij_wiadomosc(adres_serwera, numer_portu, wiadomosc):
    try:
        # Utworzenie gniazda TCP
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Rozwiązanie nazwy hosta na adres IP, jeśli to konieczne
        adres_ip = socket.gethostbyname(adres_serwera)

        # Połączenie z serwerem na danym porcie
        gniazdo.connect((adres_ip, numer_portu))

        # Uzupełnianie lub przycinanie wiadomości do 20 znaków
        if len(wiadomosc) < 20:
            wiadomosc = wiadomosc.ljust(20)
        elif len(wiadomosc) > 20:
            wiadomosc = wiadomosc[:20]

        # Wysłanie wiadomości do serwera
        print(f"Wysyłanie wiadomości: '{wiadomosc}'")
        gniazdo.sendall(wiadomosc.encode())

        # Odbiór odpowiedzi od serwera
        odpowiedz = gniazdo.recv(20)  # Odbiór dokładnie 20 bajtów
        print(f"Otrzymano odpowiedź: '{odpowiedz.decode().strip()}'")

        # Zamknięcie gniazda
        gniazdo.close()
    except socket.error as err:
        print(f"Błąd połączenia: {err}")

def main():
    if len(sys.argv) < 2:
        print("Użycie: python nazwa_programu.py <wiadomosc>")
        sys.exit(1)

    wiadomosc = sys.argv[1]
    adres_serwera = '212.182.24.27'
    numer_portu = 2908

    polacz_sie_z_serwerem_i_wyslij_wiadomosc(adres_serwera, numer_portu, wiadomosc)

if __name__ == "__main__":
    main()