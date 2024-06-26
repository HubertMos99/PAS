import socket
import sys

def send_all(sock, message):
    total_sent = 0
    message_length = len(message)
    while total_sent < message_length:
        sent = sock.send(message[total_sent:])
        if sent == 0:
            raise RuntimeError("Połączenie zerwane")
        total_sent += sent

def recv_all(sock, length):
    chunks = []
    total_received = 0
    while total_received < length:
        chunk = sock.recv(min(length - total_received, 2048))
        if chunk == b'':
            raise RuntimeError("Połączenie zerwane")
        chunks.append(chunk)
        total_received += len(chunk)
    return b''.join(chunks)

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

        # Wysłanie całej wiadomości do serwera
        print(f"Wysyłanie wiadomości: '{wiadomosc}'")
        send_all(gniazdo, wiadomosc.encode())

        # Odbiór całej odpowiedzi od serwera
        odpowiedz = recv_all(gniazdo, 20)  # Odbiór dokładnie 20 bajtów
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