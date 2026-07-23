# n - broj timova
# k - broj grupa
# m - broj timova koji prolazi u narednu fazu
# p - broj timova koji prolazi direktno u narednu fazu iz svake grupe
# q - broj najbolje plasiranih timova iz svih grupa koji su zauzeli p+1 mesto u svojoj grupi

# q < k
# m = p * k + q

# svaki tuple u listi rez -> (tim, grupa, broj bodova, gol razlika)

# List comprehension sintaksa za ugnjezdene petlje:
# nova_lista = [izraz for x in spoljasnja for y in unutrasnja]

def prolazak_1(rez:list[tuple[str, int, int, int]], n:int, k:int, m:int, p:int, q:int) -> list[str]:
    # grupisemo timove u njihove odgovarajuce grupe tako sto kreiramo listu listi
    # u prvoj podlisti su svi timovi iz grupe 1, u drugoj podlisti su svi timovi iz grupe 2 itd.
    # u svakoj grupi timovi su sortirani po broju bodova i po gol razlici u opadajucem redosledu
    timovi_po_grupama = [
        sorted((tim for tim in rez if tim[1] == grupa + 1), key=lambda x: (x[2], x[3]), reverse=True) 
        for grupa in range(k)
    ]

    # uzimamo prvih p timova iz svake grupe koji direktno prolaze dalje
    direktno_prosli_timovi = [tim[0] for grupa in timovi_po_grupama for tim in grupa[:p]]

    # od timova sa p+1 mesta iz svake grupe pravimo novu listu (grupu) tako sto ih sortiramo
    # po broju bodova i gol razlici u opadajucem redosledu
    # ako postoje timovi sa p+2, p+3, itd. mesta u grupama oni se ignorisu jer sigurno ne prolaze dalje
    timovi_kandidati_za_prolazak = sorted(
        (grupa[p] for grupa in timovi_po_grupama if len(grupa) > p),
        key=lambda tim: (tim[2], tim[3]), reverse=True
    )

    # od timova sa p+1 mesta iz svih grupa dodatna prolaze q najboljih po bodovima i gol razlici
    dodatno_prosli_timovi = [tim[0] for tim in timovi_kandidati_za_prolazak[:q]]

    prosli_timovi = direktno_prosli_timovi + dodatno_prosli_timovi
    return prosli_timovi

if __name__ == "__main__":
    prosli_timovi = prolazak_1(rez=[("T1", 1, 3, 1), ("T2", 3, 7, 4), ("T3", 2, 6, 1), ("T4", 2, 3, 0),
             ("T5", 3, 5, 2), ("T6", 1, 4, 1), ("T7", 1, 4, 2), ("T8", 1, 6, 3),
             ("T9", 2, 9, 7), ("T10", 3, 1, -2), ("T11", 3, 3, -1), ("T12", 2, 0, -4)],
             n=12, k=3, m=8, p=3, q=2)
    print(prosli_timovi)