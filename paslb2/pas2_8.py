import sys
import socket
from concurrent.futures import ThreadPoolExecutor


def sprawdz_port(adres_serwera, port, timeout=1):
    try:
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gniazdo.settimeout(timeout)
        adres_ip = socket.gethostbyname(adres_serwera)
        gniazdo.connect((adres_ip, port))
        gniazdo.close()

        # Uzyskanie nazwy usługi, jeśli jest znana
        try:
            usluga = socket.getservbyport(port, 'tcp')
        except OSError:
            usluga = 'nieznana usługa'

        return (port, usluga)
    except (socket.timeout, socket.error):
        return None


def skanuj_porty(adres_serwera, start_port=1, end_port=1024, max_workers=100):
    print(f"Skanowanie serwera {adres_serwera} na portach od {start_port} do {end_port}...")
    otwarte_porty = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(sprawdz_port, adres_serwera, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                otwarte_porty.append(result)

    return otwarte_porty


def main():
    if len(sys.argv) < 2:
        print("Użycie: python nazwa_programu.py <adres_serwera> [początkowy_port] [końcowy_port]")
        sys.exit(1)

    adres_serwera = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    otwarte_porty = skanuj_porty(adres_serwera, start_port, end_port)

    if otwarte_porty:
        print(f"Otwarty porty na serwerze {adres_serwera}:")
        for port, usluga in otwarte_porty:
            print(f"  - Port {port}: {usluga}")
    else:
        print(f"Brak otwartych portów na serwerze {adres_serwera} w zakresie {start_port}-{end_port}.")


if __name__ == "__main__":
    main()