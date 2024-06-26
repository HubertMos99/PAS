import socket

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def hex_to_ip(hex_str):
    octets = [str(hex_to_dec(hex_str[i:i+2])) for i in range(0, len(hex_str), 2)]
    return ".".join(octets)

def extract_ip_fields(hex_packet):
    version_hex = hex_packet[:1]
    version = hex_to_dec(version_hex) >> 4

    src_ip_hex = hex_packet[24:32]
    src_ip = hex_to_ip(src_ip_hex)

    dst_ip_hex = hex_packet[32:40]
    dst_ip = hex_to_ip(dst_ip_hex)

    protocol_hex = hex_packet[18:20]
    protocol = hex_to_dec(protocol_hex)

    return version, src_ip, dst_ip, protocol

def extract_tcp_udp_fields(hex_packet, protocol):
    if protocol == 6:  # TCP
        header_size = 40  # 20 bajtów IP + 20 bajtów nagłówka TCP (bez opcji)
        src_port_hex = hex_packet[40:44]
        dst_port_hex = hex_packet[44:48]
    elif protocol == 17:  # UDP
        header_size = 28  # 20 bajtów IP + 8 bajtów nagłówka UDP
        src_port_hex = hex_packet[40:44]
        dst_port_hex = hex_packet[44:48]
    else:
        raise ValueError("Unsupported protocol")

    src_port = hex_to_dec(src_port_hex)
    dst_port = hex_to_dec(dst_port_hex)
    data_hex = hex_packet[header_size*2:]
    data = bytes.fromhex(data_hex).decode('utf-8')

    return src_port, dst_port, data

def send_message(message, server_address, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode('utf-8'), (server_address, server_port))
        response, _ = sock.recvfrom(1024)
        return response.decode('utf-8')
    finally:
        sock.close()

# Zadany pakiet IP w zapisie szesnastkowym
hex_packet = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"

# Wydobycie pól z pakietu IP
version, src_ip, dst_ip, protocol = extract_ip_fields(hex_packet)

# Przygotowanie wiadomości typu A
message_a = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"
print("Wiadomość typu A do wysłania:", message_a)

# Parametry serwera
server_address = "212.182.24.27"
server_port_a = 2911

# Wysłanie wiadomości typu A i odbiór odpowiedzi
response_a = send_message(message_a, server_address, server_port_a)
print("Odpowiedź serwera (A):", response_a)

if response_a == "TAK":
    # Wydobycie pól TCP/UDP z pakietu
    src_port, dst_port, data = extract_tcp_udp_fields(hex_packet, protocol)

    # Przygotowanie wiadomości typu B
    message_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"
    print("Wiadomość typu B do wysłania:", message_b)

    # Wysłanie wiadomości typu B i odbiór odpowiedzi
    response_b = send_message(message_b, server_address, server_port_a)
    print("Odpowiedź serwera (B):", response_b)
else:
    print("Odpowiedź serwera (A) nie była TAK, nie wysłano wiadomości typu B")