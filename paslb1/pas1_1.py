nazwa_pliku = input("Podaj nazwę pliku tekstowego do skopiowania: ")

plik_docelowy = "lab1zad1.txt"

try:
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik_zrodlowy:
        zawartosc = plik_zrodlowy.read()

    with open(plik_docelowy, 'w', encoding='utf-8') as plik_docelowy:
        plik_docelowy.write(zawartosc)

    print(f"Plik {nazwa_pliku} został skopiowany do {plik_docelowy.name}")

except FileNotFoundError:
    print(f"Błąd: Plik o nazwie {nazwa_pliku} nie istnieje.")
except IOError as e:
    print(f"Błąd: Nie można odczytać lub zapisać pliku. {e}")