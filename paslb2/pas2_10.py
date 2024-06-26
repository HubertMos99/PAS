import socket
import sys

def wyslij_hostname_i_odbierz_ip(hostname, serwer_adres, serwer_port):
    try:
        # Utworzenie gniazda UDP
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        gniazdo.settimeout(10)

        # Wysłanie nazwy hostname do serwera
        print(f"Wysyłanie hostname '{hostname}' do serwera {serwer_adres}:{serwer_port}")
        gniazdo.sendto(hostname.encode(), (serwer_adres, serwer_port))

        # Odbiór odpowiedzi od serwera
        odpowiedz, _ = gniazdo.recvfrom(1024)
        ip_adres = odpowiedz.decode()
        print(f"Otrzymano adres IP: {ip_adres}")

        # Zamknięcie gniazda
        gniazdo.close()
    except socket.timeout:
        print("Operacja przekroczyła limit czasu")
    except socket.error as err:
        print(f"Błąd socketu: {err}")


def main():
    if len(sys.argv) != 2:
        print("Użycie: python nazwa_programu.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    serwer_adres = '212.182.24.27'
    serwer_port = 2907

    wyslij_hostname_i_odbierz_ip(hostname, serwer_adres, serwer_port)

if __name__ == "__main__":
    main()