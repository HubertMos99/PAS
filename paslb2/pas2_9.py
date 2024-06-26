import socket
import sys


def wyslij_ip_i_odbierz_hostname(adres_ip, serwer_adres, serwer_port):
    try:
        # Utworzenie gniazda UDP
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        gniazdo.settimeout(10)

        # Wysłanie adresu IP do serwera
        print(f"Wysyłanie adresu IP {adres_ip} do serwera {serwer_adres}:{serwer_port}")
        gniazdo.sendto(adres_ip.encode(), (serwer_adres, serwer_port))

        # Odbiór odpowiedzi od serwera
        odpowiedz, _ = gniazdo.recvfrom(1024)
        hostname = odpowiedz.decode()
        print(f"Otrzymano hostname: {hostname}")

        # Zamknięcie gniazda
        gniazdo.close()
    except socket.timeout:
        print("Operacja przekroczyła limit czasu")
    except socket.error as err:
        print(f"Błąd socketu: {err}")


def main():
    if len(sys.argv) != 2:
        print("Użycie: python nazwa_programu.py <adres_ip>")
        sys.exit(1)

    adres_ip = sys.argv[1]
    serwer_adres = '212.182.24.27'
    serwer_port = 2906

    wyslij_ip_i_odbierz_hostname(adres_ip, serwer_adres, serwer_port)


if __name__ == "__main__":
    main()