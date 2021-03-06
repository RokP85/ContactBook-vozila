# -*- coding: utf-8 -*-

class oseba(object):
    def __init__(self, ime, priimek, naslov, tel):
        self.ime = ime
        self.priimek = priimek
        self.naslov = naslov
        self.tel = tel

    def izpis(self):
        return self.ime, self.priimek, self.naslov, self.tel


def dodaj_nov_kontakt(kontakti):
    while True:
        ime = raw_input("Vnesite ime:")
        priimek = raw_input("vnesite priimek:")
        naslov = raw_input("Vnesite naslov:")
        tel= raw_input("Vnesite telefonsko številko:")

        nov_kontakt = oseba(ime=ime, priimek=priimek, naslov=naslov, tel=tel)
        kontakti.append(nov_kontakt)
        print "Nov kontakt dodan"

        nadaljuj = raw_input("Želite dodati se en kontakt [DA/NE]?")
        if nadaljuj == "NE":
            main()

def seznam_kontaktov(kontakti):
    for kontakt in kontakti:
        print kontakt.izpis()
    main()

def urejanje_kontakta(kontakti):

    while True:
        podatek = raw_input("Vnesi ime, priimek, naslov ali tel. osebe:")
        if podatek in kontakti:
            print kontakti[oseba](podatek)
            popravek = raw_input("Kaj želite popraviti[ime, priimek, naslov, tel]?")
            if popravek == "ime":
                novo_ime = raw_input("Vnesite novo ime:")
                oseba.ime = novo_ime
                print "Novo ime vnešeno"
            elif popravek == "priimek":
                nov_priimek = raw_input("Vnesite nov priimek:")
                oseba.priimek = nov_priimek
                print "Nov priimek vnešen"
            elif popravek == "naslov":
                nov_naslov = raw_input("Vnesite nov naslov:")
                oseba.naslov = nov_naslov
                print "Nov naslov vnešen"
            else:
                print "Vnesli ste napačen podatek ali pa osebe ni v imeniku"

            nadaljuj = raw_input("Želite še kaj spremeniti [DA/NE]?")
            if nadaljuj == "NE":
                main()

def izbris_kontakta(kontakti):
    podatek = raw_input("Vnesite ime, priimek, naslov ali tel kontakta za izbris:")
    if podatek in kontakti:
        kontakti.remove(oseba)
    nadaljuj = raw_input("Želite izbrisati še kakšen kontakt [DA/NE]?")
    if nadaljuj == "NE":
        main()


def main():
    print "Contact Book"
    print "Dodaj nov kontkat - a"
    print "Seznam kontaktov - b"
    print "Urejanje kontakta -c"
    print "Izbris kontakta -d"
    print "Izhod iz imenika -e"

    kontakti = []

    izbira = raw_input("Kaj želite narediti?")
    if izbira == "a":
        dodaj_nov_kontakt(kontakti)
    elif izbira == "b":
        seznam_kontaktov(kontakti)
    elif izbira == "c":
        urejanje_kontakta(kontakti)
    elif izbira == "d":
        izbris_kontakta(kontakti)
    elif izbira == "e":
        exit()

if __name__ == "__main__":
    main()
