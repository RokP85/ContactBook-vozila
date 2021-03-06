# -*- coding: utf-8 -*-

class vozilo(object):
    def __init__(self, znamka, model, st_km, datum_servisa, registrska):
        self.znamka_vozila = znamka
        self.model_vozila = model
        self.st_prevozenih_km = st_km
        self.datum_zadnjega_servisa = datum_servisa
        self.registrska_oznaka = registrska

def seznam_vseh_vozil(vozila):
        with open("VOZILA.txt", "r") as file:
            for vozilo in file:
                print vozilo

def urejanje_st_km(vozila):
    iskanje = raw_input("Vnesite znake registrske tablice vozila:")
    for vozilo in vozila:
        if vozilo.registrska_oznaka == iskanje:
            popis_km = int(raw_input("Vnesite št. kilometrov:"))
            vozilo.st_prevozenih_km = popis_km
            print "Vnos zaključen"
            break

def urejanje_datum_servis(vozila):
    iskanje = raw_input("Vnesite znake registrske tablice vozila:")
    for vozilo in vozila:
        if vozilo.registrska_oznaka == iskanje:
            datum_servis = raw_input("Vnesite datum zadnjega servisa:")
            vozilo.datum_zadnjega_servisa = datum_servis
            print "Vnos zaključen"
            break

def dodaj_novo_vozilo(vozila):
    znamka = raw_input("Vnesite znamko vozila:")
    model = raw_input("Vnesite model vozila:")
    st_km = raw_input("Vnesite št. prevoženih km:")
    datum_servisa = raw_input("Vnesite datum zadnjega servisa vozila:")
    registrska = raw_input("Vnesite registrsko oznako vozila:")

    novo_vozilo = vozilo(znamka=znamka, model=model, st_km=st_km, datum_servisa=datum_servisa, registrska=registrska)
    vozila.append(novo_vozilo)
    print "Novo vozilo vnešeno"


def izbris_vozila(vozila):
    iskanje = raw_input("Vnesite registrsko oznako vozila, ki ga želite izbrisati:")
    vozilo.registrska = iskanje
    for vozilo.registrska in vozila:
        vozila.remove(vozilo)
        print "Vozilo odstranjeno iz seznama"
        break

def shranjevanje(vozila):
    with open("VOZILA.txt", "w") as file:
        for vozilo in vozila:
            file.write("Znamka vozila: %s, Model vozila: %s, Št. prevoženih km: %s, Datum zadnjega servisa: %s, " \
                       "Registrska oznaka: %s\n" % (vozilo.znamka_vozila, vozilo.model_vozila, vozilo.st_prevozenih_km,
                                                    vozilo.datum_zadnjega_servisa, vozilo.registrska_oznaka))
    print "Vnosi so shranjeni"


def main():
    vozila = []

    while True:
        print "Ogled seznama vseh vozil z vsemi podatki ali pa podatki za določeno vozilo - opcija a"
        print "Urejanje števila prevoženih km za vozila - opcija b"
        print "Urejanje datuma servisa za vozila - opcija c"
        print "Dodaj novo vozilo - opcija d"
        print "Izbris vozila s seznama - opcija e"
        print "Za shranjevanje vseh sprememb - opcija f"
        print "Izhod iz programa g"

        izbor_storitve = raw_input("Izberite željeno storitev (opcijo) z vnosom črke s seznama:")

        if izbor_storitve == "a":
            seznam_vseh_vozil(vozila)
        elif izbor_storitve == "b":
            urejanje_st_km(vozila)
        elif izbor_storitve == "c":
            urejanje_datum_servis(vozila)
        elif izbor_storitve == "d":
            dodaj_novo_vozilo(vozila)
        elif izbor_storitve == "e":
            izbris_vozila(vozila)
        elif izbor_storitve == "f":
            shranjevanje(vozila)
        elif izbor_storitve == "g":
            print "Izhod iz programa"
            break
        else:
            print "Niste vnesli storitve s seznama, prosim ponovite vnos"


if __name__ == "__main__":
    main()
