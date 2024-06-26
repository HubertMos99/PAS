import socket

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def extract_udp_fields(hex_datagram):
    # Numer portu źródłowego (pierwsze 4 bajty)
    src_port_hex = hex_datagram[:4]
    src_port = hex_to_dec(src_port_hex)

    # Numer portu docelowego (kolejne 4 bajty)
    dst_port_hex = hex_datagram[4:8]
    dst_port = hex_to_dec(dst_port_hex)

    # Dane (reszta pakietu)
    data_hex = hex_datagram[16:]
    data = bytes.fromhex(data_hex).decode('utf-8')

    return src_port, dst_port, data

# Zadany datagram UDP w zapisie szesnastkowym
hex_datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"

# Wydobycie pól z datagramu
src_port, dst_port, data = extract_udp_fields(hex_datagram)

# Przygotowanie wiadomości do wysłania
message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"
print("Wiadomość do wysłania:", message)

# Parametry serwera
server_address = "127.0.0.1"
server_port = 2909

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