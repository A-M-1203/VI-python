# List comprehension je sazetiji nacin da se kreira lista na osnovu neke druge iterabilne strukture (liste, range-a, stringa...)
# umesto da se koristi klasicna for petlja sa .append()

# Osnovna sintaksa:
# nova_lista = [izraz for element in iterabilni_objekat]

# izraz – sta se dodaje u novu listu (moze da bude sam element ili neka transformacija nad njim)
# element – promenljiva koja prolazi kroz svaki clan iterabilnog objekta
# iterabilni_objekat – lista, range, string, itd. kroz koji se iterira

# Primer:
# kvadrati = [x**2 for x in range(1, 6)]
# print(kvadrati)  ->  [1, 4, 9, 16, 25]

# Ekvivalentno ovome:
# kvadrati = []
# for x in range(1, 6):
#    kvadrati.append(x**2)

# Sintaksa sa uslovom (filtriranje):
# nova_lista = [izraz for element in iterabilni_objekat if uslov]

# Primer (samo parni brojevi):
# parni = [x for x in range(10) if x % 2 == 0]
# print(parni)  ->  [0, 2, 4, 6, 8]

def najstabilniji_dan(podaci:list[tuple[str, int, int]]) -> str|None:
    # prosecna temperatura za jedan dan je minimalna temperatura tog dana + maksimalna temperatura tog dana / 2
    # prosecna temperatura svih dana je kada saberemo prosecne temperature svakog dana i podelimo sa brojem dana
    ukupna_prosecna_temperatura = sum((min_temp + max_temp) / 2 for _, min_temp, max_temp in podaci) / len(podaci)

    # u razmatranje ulaze samo dani cija je prosecna temperatura veca od prosecne temperature svih dana
    dani_kandidati = [(dan, max_temp-min_temp) for dan, min_temp, max_temp in podaci if (min_temp + max_temp) / 2 > ukupna_prosecna_temperatura]

    # ako nema nijednog takvog dana onda funkcija vraca None
    if not dani_kandidati:
        return None

    # najstabilniji je dan kod koga je najmanja razlika izmedju maksimalne i minimalne temperature tog dana
    najstabilniji_dan = min(dani_kandidati, key=lambda x: x[1])
    return najstabilniji_dan[0]

if __name__ == "__main__":
    print(najstabilniji_dan([("Ponedeljak", 10, 20), ("Utorak", 12, 18), ("Sreda", 15, 25),
                       ("Cetvrtak", 14, 19), ("Petak", 13, 17)]))