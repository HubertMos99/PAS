import socket

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def extract_tcp_fields(hex_segment):
    # Numer portu źródłowego (pierwsze 4 bajty)
    src_port_hex = hex_segment[:4]
    src_port = hex_to_dec(src_port_hex)

    # Numer portu docelowego (kolejne 4 bajty)
    dst_port_hex = hex_segment[4:8]
    dst_port = hex_to_dec(dst_port_hex)

    # Rozmiar nagłówka TCP: przeskok do początku danych (32 bity, 20 bajtów nagłówka + 12 bajtów opcji = 32 bajty)
    header_size = 32 * 2  # 32 bajty, każdy bajt reprezentowany przez 2 znaki szesnastkowe
    data_hex = hex_segment[header_size:]
    data = bytes.fromhex(data_hex).decode('utf-8')

    return src_port, dst_port, data

# Zadany segment TCP w zapisie szesnastkowym
hex_segment = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"

# Wydobycie pól z segmentu
src_port, dst_port, data = extract_tcp_fields(hex_segment)

# Przygotowanie wiadomości do wysłania
message = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"
print("Wiadomość do wysłania:", message)

# Parametry serwera
server_address = "212.182.24.27"
server_port = 2910

# Utworzenie gniazda UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Wysłanie wiadomości do serwera
    sock.sendto(message.encode('utf-8'), (server_address, server_port))

    # Odbiór odpowiedzi od serwera
    response, _ = sock.recvfrom(1024)
    print("Odpowiedź serwera:", response.decode('utf-8'))
finally:
    # Zamknięcie gniazda
    sock.close()