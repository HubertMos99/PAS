import socket
import sys
from time import strftime, gmtime

HOST = '127.0.0.1'
PORT = 2911
def check_msgA_syntax(message):
    s = len(message.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        parts = message.split(";")
        if parts[0] == "zad15odpA" and parts[1] == "ver" and parts[3] == "srcip" and parts[5] == "dstip" and parts[7] == "type":
            try:
                ver = int(parts[2])
                src_ip = parts[4]
                dst_ip = parts[6]
                protocol_type = int(parts[8])

                if ver == 4 and protocol_type == 6 and src_ip == "212.182.24.27" and dst_ip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except ValueError:
                return "NIE"
        else:
            return "BAD_SYNTAX"


def check_msgB_syntax(message):
    parts = message.split(";")
    if len(parts) != 7:
        return "BAD_SYNTAX"

    if parts[0] == "zad15odpB" and parts[1] == "srcport" and parts[3] == "dstport" and parts[5] == "data":
        try:
            src_port = int(parts[2])
            dst_port = int(parts[4])
            data = parts[6]

            if src_port == 2900 and dst_port == 47526 and data == "network programming is fun":
                return "TAK"
            else:
                return "NIE"
        except ValueError:
            return "NIE"
    else:
        return "BAD_SYNTAX"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print(f'Powiązanie nieudane. Kod błędu: {msg.errno} Wiadomość: {msg.strerror}')
    sys.exit()

print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Serwer UDP nasłuchuje na {HOST}:{PORT}")

try:
    while True:
        data, address = sock.recvfrom(1024)
        data = data.decode()
        print(
            f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Otrzymano {len(data)} bajtów od klienta {address}. Treść: {data}')

        if data:
            parts = data.split(";")
            print(f"TREŚĆ: {data}")

            if parts[0] == "zad15odpA":
                answer = check_msgA_syntax(data)
                sent = sock.sendto(answer.encode(), address)
                print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Wysłano {sent} bajtów do klienta {address}.')

            elif parts[0] == "zad15odpB":
                answer = check_msgB_syntax(data)
                sent = sock.sendto(answer.encode(), address)
                print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Wysłano {sent} bajtów do klienta {address}.')

            else:
                sent = sock.sendto("BAD_SYNTAX".encode(), address)
                print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Wysłanot {sent} bajtów do klienta {address}.')
finally:
    sock.close()
