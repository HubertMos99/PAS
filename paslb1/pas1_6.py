import sys
import socket

def polacz_sie_z_serwerem(adres_serwera, numer_portu):
    try:
        # Utworzenie gniazda TCP
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Rozwiązanie nazwy hosta na adres IP, jeśli to konieczne
        adres_ip = socket.gethostbyname(adres_serwera)

        # Połączenie z serwerem na danym porcie
        gniazdo.connect((adres_ip, numer_portu))

        # Jeśli połączenie się powiedzie
        print(f"Połączenie z {adres_serwera} ({adres_ip}) na porcie {numer_portu} powiodło się.")
        gniazdo.close()
    except socket.error as err:
        print(f"Nie udało się połączyć z {adres_serwera} na porcie {numer_portu}: {err}")

def main():
    # Sprawdzenie, czy podano odpowiednią liczbę argumentów
    if len(sys.argv) != 3:
        print("Użycie: python nazwa_programu.py <adres_serwera> <numer_portu>")
        sys.exit(1)

    # Pobranie adresu serwera i numeru portu z argumentów linii poleceń
    adres_serwera = sys.argv[1]
    try:
        numer_portu = int(sys.argv[2])
    except ValueError:
        print("Numer portu musi być liczbą całkowitą.")
        sys.exit(1)

    # Połączenie z serwerem
    polacz_sie_z_serwerem(adres_serwera, numer_portu)

if __name__ == "__main__":
    main()