# n - broj timova
# k - broj grupa
# m - broj timova koji prolazi u narednu fazu
# p - broj timova koji prolazi direktno u narednu fazu iz svake grupe
# q - broj najbolje plasiranih timova iz svih grupa koji su zauzeli p+1 mesto u svojoj grupi

# q < k
# m = p * k + q

# svaki tuple u listi rez -> (tim, grupa, broj bodova, gol razlika)

from itertools import chain

def prolazak(rez:list[tuple[str, int, int, int]], n:int, k:int, m:int, p:int, q:int) -> list[str]:
    # prvo treba da odredimo p * k timova koji direktno prolaze u narednu fazu

    # pravimo po jednu listu za svaku grupu (ukupno k grupa)
    timovi_po_grupama = [[] for _ in range(k)]

    # stavljamo timove u odgovarajuce grupe (liste) npr. grupa 1 -> timovi_po_grupama[0], grupa 2 -> timovi_po_grupama[2]
    for tim in rez:
        grupa = tim[1]
        timovi_po_grupama[grupa - 1].append(tim)

    timovi_koji_su_prosli = []
    # u svakoj grupi sortiramo timove po broju bodova, pa onda po gol razlici u opadajucem redosledu
    # tako da je prvi tim u grupi onaj sa najvise bodova
    # (ili sa najboljom gol razlikom ako u grupi ima dva tima sa istim brojem bodova)
    # onda brisemo timove od p+1 mesta pa do kraja grupe jer oni sigurno ne prolaze
    # npr. ako prolaze prva k=3 tima iz svake grupe onda od ostalih timova koji nisu zauzeli jedno od
    # prva tri mesta u svojoj grupi ulaze u razmatranje za prolaz samo timovi koji su zauzeli k+1=4 mesto
    # u svojoj grupi
    # u ugnjezdenoj petlji uzimamo samo timove koji direktno prolaze npr. ako je k=3 onda prva 3 tima iz svake grupe
    for grupa in timovi_po_grupama:
        grupa.sort(key=lambda tim: (tim[2], tim[3]), reverse=True)
        del grupa[p+1:]
        for _ in range(p):
            tim_koji_direktno_prolazi = grupa.pop(0)
            timovi_koji_su_prosli.append(tim_koji_direktno_prolazi[0])

    # spajamo sve preostale timove u jednu listu (grupu)
    preostali_timovi = list(chain.from_iterable(timovi_po_grupama))
    # sortiramo ih tako da je prvi tim u listi (grupi) onaj sa najvise bodova
    # (ili sa najboljom gol razlikom ako ima vise timova sa istim brojem bodova)
    preostali_timovi.sort(key=lambda tim: (tim[2], tim[3]), reverse=True)
    # od preostalih timova uzimamo jos q najboljih za prolaz
    for _ in range(q):
        tim_koji_dodatno_prolazi = preostali_timovi.pop(0)
        timovi_koji_su_prosli.append(tim_koji_dodatno_prolazi[0])

    return timovi_koji_su_prosli

if __name__ == "__main__":
    timovi_koji_su_prosli = prolazak(rez=[("T1", 1, 3, 1), ("T2", 3, 7, 4), ("T3", 2, 6, 1), ("T4", 2, 3, 0),
            ("T5", 3, 5, 2), ("T6", 1, 4, 1), ("T7", 1, 4, 2), ("T8", 1, 6, 3),
            ("T9", 2, 9, 7), ("T10", 3, 1, -2), ("T11", 3, 3, -1), ("T12", 2, 0, -4)],
            n=12, k=3, m=8, p=3, q=2)
    print(timovi_koji_su_prosli)