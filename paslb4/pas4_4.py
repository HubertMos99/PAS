import socket

HOST = '127.0.0.1'
PORT = 65432


def calculate(expression):
    try:
        # Rozdzielenie danych na składniki: liczba1, operator, liczba2
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return 'Błąd: Dzielenie przez zero!'
            return num1 / num2
        else:
            return 'Błąd: Nieznany operator!'
    except ValueError:
        return 'Błąd: Nieprawidłowe dane wejściowe!'


# Tworzenie gniazda (socketu) UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Serwer kalkulatora UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)  # Odbieranie danych od klienta i adresu nadawcy
        expression = data.decode()
        print(f"Otrzymano od {addr}: {expression}")

        # Obliczenie wyniku
        result = calculate(expression)
        result_str = str(result)
        print(f"Odsyłanie wyniku: {result_str}")

        # Odesłanie wyniku z powrotem do klienta
        s.sendto(result_str.encode(), addr)
