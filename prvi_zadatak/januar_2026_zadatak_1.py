def prebroji(tekst:str, limit:int) -> list[str]:
    # kreiramo set na osnovu stringa tekst sto izvlaci pojedinacne karaktere iz stringa i ubacuje ih u set
    # kada pokusa da se doda karakter koji je vec u set-u nista se ne desava jer set ne dozvoljava duplikate
    # time dobijamo jedinstvene karaktere iz teksta, onda za svaki karakter iz set-a nalazimo koliko se on puta
    # javlja u tekstu sa tekst.count(karakter) i ako je taj broj veci od limita ubacujemo taj karakter u listu koju vracamo iz funkcije
    # umesto set(tekst) moze da se koristi i dict.fromkeys(tekst) ako je bitan redosled pojavljivanja karaktera u rezultujucoj listi
    karakteri_preko_limita = [
        karakter for karakter in set(tekst) 
        if tekst.count(karakter) > limit
    ]
    return karakteri_preko_limita

if __name__ == "__main__":
    karakteri_preko_limita = prebroji("aabcdd", 1)
    print(karakteri_preko_limita)