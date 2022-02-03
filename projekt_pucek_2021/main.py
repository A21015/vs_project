# Třída obsahující metody pro převody
class Prevod:
    def __init__(self):
        pass

    # Metoda pro převod z arabských čísel na římská
    @staticmethod
    def narim(nrcislo):
        if 4000 > nrcislo > 0:

            # List hodnot, použitých při převodu
            hod = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]

            # List obsahující možné symboly a kombinace vyjímek
            sym = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
            ]
            nrrimske = ''
            i = 0

            # Dokud nejsou převedeny všechny čísla, provádí se převod
            while nrcislo > 0:
                for _ in range(nrcislo // hod[i]):
                    nrrimske += sym[i]
                    nrcislo -= hod[i]
                i += 1
            return nrrimske
            # Návratová hodnota výsledku

        # Pokud není splněna podmínka, program zahlásí chybu
        else:
            print("Chybně zadané číslo.")
            return " "  # Vrátí zpět pouze mezeru

    # Metoda pro převod z římských čísel na arabské
    @staticmethod
    def naar(s):
        # Podmínka pro ošetření vstupu při vložení prázdné hodnoty
        if s != 0:
            # Seznam možných symbolů a vyjímek při převodu
            narim = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000,
                     'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}
            j = 0
            nacislo = 0

            # Cyklus, který opakuje, dokud proměnná j
            # není menší, než délka vstupního stringu
            while j < len(s):
                # Podmínka pro převod vyjímek ze seznamu výše
                if j + 1 < len(s) and s[j:j + 2] in narim:
                    nacislo += narim[s[j:j + 2]]
                    j += 2

                # Pokud se nenachází vyjímka pro
                # převod, provede se klasický jednočíselný
                else:
                    nacislo += narim[s[j]]
                    j += 1
            return nacislo  # Návratová hodnota výsledku

        # Je-li odeslána prázdná hodnota římského čísla, program zahlásí chybu
        else:
            print("Chybně zadané číslo.")
            return 0


def test_prevod():
    """Testovací příkazy."""
    assert Prevod().narim(3999) == "MMMCMXCIX"
    assert Prevod().naar("MMMCMXCIX") == 3999


if __name__ == "__main__":
    # Deklarace proměnné typu string,
    # která následně určuje, jestli se má program ukončit
    zadani = " "
    c = 0

    # Cyklus, při kterém program běží, dokud
    # není na konci zadáno A pro ukončení
    while zadani != 'a':
        rimZad = "15"
        arZad = 0
        rim = 0
        d = 0

        # Cyklus, při kterém běží input do doby,
        # než uživatel zadá validní hodnotu
        while rim < 1 or rim > 3999:
            # rimZad = input("Zadej římské: ")
            print(str("Zadej římské: ") + str(rimZad))
            x = rimZad.isnumeric()

            # Obsahuje-li římské zadání číslo, jedná se o chybu
            if x == 1:
                print("Nezadal jsi římské číslo.")
                rimZad = "MMMMM"

            # Pokud je vše zadáno správně, program pokračuje dál
            else:
                if rimZad.islower():
                    rimZad = rimZad.upper()
                rim = Prevod().naar(rimZad)

                # Pokud se výsledek nachází v intervalu
                # pro platnost, program vypíše výsledek
                if 0 < rim < 4000:
                    print(rimZad + str(" = ") + str(rim))

                # Je-li výsledná hodnota mimo interval
                # pro platnost, program zahlásí chybu
                else:
                    print("Chybné zadání.")
                    rimZad = "MMMDCCCLXXXVIII"

        # Cyklus, který běží po dobu, dokud není správně zadané číslo
        while arZad < 1 or arZad > 3999:
            # arZad = str(input("Zadej arabské: "))
            if d == 0:
                arZad = "XCIV"
            if d == 1:
                arZad = "5621"
            if d == 2:
                arZad = "3888"
            print(str("Zadej arabské: ") + str(arZad))

            # Kontrola, jestli bylo správně zadáno číslo v zadání
            if arZad.isnumeric():
                arZad = int(arZad)
                # Převod proměnné typu string na integer

                # Pokud se zadané číslo nenachází v
                # platném rozsahu, program zahlásí chybu
                if arZad < 1 or arZad > 3999:
                    print("Chybné zadání.")
                    d = 2

                # V opačném případě se provede převod
                else:
                    print(str(arZad) + str(" = ") + Prevod().narim(arZad))

            # Nebylo-li zadáno číslo, program zahlásí chybu
            else:
                print("Nezadal jsi číslo.")
                arZad = 0
                # Zápis hodnoty, aby při špatném zadání neskončil cyklus
                d = 1

        # Ukončovací dialog programu
        # zadani = input("Přejete si ukončit program? (A/N)\n")
        if c == 0:
            zadani = "N"
        elif c == 1:
            zadani = "A"
        print(str("Přejete si ukončit program? (A/N)\n") + str(zadani))
        c = 1
        # Podmínka pro not-case-sensitive zadání pro ukončení
        if zadani.isupper():
            zadani = zadani.lower()
            # Převod velkého písmena na malé
