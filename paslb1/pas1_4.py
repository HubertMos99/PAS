import sys
import socket

def uzyskaj_hostname(adres_ip):
    try:
        # Pobranie nazwy hosta dla podanego adresu IP
        hostname, aliasy, adresy_ip = socket.gethostbyaddr(adres_ip)
        return hostname
    except socket.herror:
        return None

def main():
    # Sprawdzenie, czy podano odpowiednią liczbę argumentów
    if len(sys.argv) != 2:
        print("Użycie: python nazwa_programu.py <adres_ip>")
        sys.exit(1)

    # Pobranie adresu IP z argumentów linii poleceń
    adres_ip = sys.argv[1]

    # Uzyskanie i wyświetlenie nazwy hosta
    hostname = uzyskaj_hostname(adres_ip)
    if hostname:
        print(f"Nazwa hosta dla adresu IP {adres_ip} to: {hostname}")
    else:
        print(f"Nie można uzyskać nazwy hosta dla adresu IP {adres_ip}")


if __name__ == "__main__":
    main()