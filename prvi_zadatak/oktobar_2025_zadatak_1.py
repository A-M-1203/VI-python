from itertools import groupby

def kreiraj_niz_B(A:list[bool]) -> list[bool]:
    # groupby grupise iste uzastopne vrednosti True/False tako sto je svaka grupa par (vrednost, iterator_elemenata)
    # npr. za listu [True, True, False, True, False, True, True, True]
    # groupby vraca grupe: (True, [T,T]), (False, [F]), (True, [T]), (False, [F]), (True, [T,T,T])
    # ako je vrednost u grupi True (if vrednost) onda proveravamo da li grupa ima paran ili neparan broj elemenata
    # ako ima paran broj elemenata onda u niz B stavljamo 1 ako ima neparan broj elemenata u niz B stavljamo 2
    # ako je vrednost False samo je ignorisemo i prelazimo na sledeci par
    B = [
        1 if len(list(grupa)) % 2 == 0 else 2 
        for vrednost, grupa in groupby(A) if vrednost
    ]
    return B

if __name__ == "__main__":
    print(kreiraj_niz_B([True, True, False, True, False, True, True, True]))
    print(kreiraj_niz_B([False, False, True, True, True, True, False, True]))
    print(kreiraj_niz_B([True, True, True, True, True, True]))