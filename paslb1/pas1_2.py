nazwa_pliku_graficznego = input("Podaj nazwę pliku graficznego do skopiowania: ")

plik_docelowy = "lab1zad1.png"

try:
    with open(nazwa_pliku_graficznego, 'rb') as plik_zrodlowy:
        zawartosc = plik_zrodlowy.read()

    with open(plik_docelowy, 'wb') as plik_docelowy:
        plik_docelowy.write(zawartosc)

    print(f"Plik {nazwa_pliku_graficznego} został skopiowany do {plik_docelowy.name}")

except FileNotFoundError:
    print(f"Błąd: Plik o nazwie {nazwa_pliku_graficznego} nie istnieje.")
except IOError as e:
    print(f"Błąd: Nie można odczytać lub zapisać pliku. {e}")