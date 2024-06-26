import sys
import socket

def uzyskaj_adres_ip(hostname):
    try:
        # Pobranie adresu IP dla podanej nazwy hosta
        adres_ip = socket.gethostbyname(hostname)
        return adres_ip
    except socket.gaierror:
        return None

def main():
    # Sprawdzenie, czy podano odpowiednią liczbę argumentów
    if len(sys.argv) != 2:
        print("Użycie: python nazwa_programu.py <hostname>")
        sys.exit(1)

    # Pobranie nazwy hosta z argumentów linii poleceń
    hostname = sys.argv[1]

    # Uzyskanie i wyświetlenie adresu IP
    adres_ip = uzyskaj_adres_ip(hostname)
    if adres_ip:
        print(f"Adres IP dla hosta {hostname} to: {adres_ip}")
    else:
        print(f"Nie można uzyskać adresu IP dla hosta {hostname}.")


if __name__ == "__main__":
    main()