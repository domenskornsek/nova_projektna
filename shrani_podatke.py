import csv


def shrani_artikle1(ime_dat, seznam_slovarjev1):
    with open(ime_dat, "w", encoding='UTF-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "stevilka",
                "link",
                "naslov_izdelka"
            ]
        )

        for artikel in seznam_slovarjev1:
            pisatelj.writerow(
                [
                    artikel["stevilka"],
                    artikel["link"],
                    artikel["naslov_izdelka"]
                ]
            )

def shrani_artikle2(ime_dat, seznam_slovarjev2):
    with open(ime_dat, "w", encoding='UTF-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "cena"
            ]
        )

        for cena in seznam_slovarjev2:
            pisatelj.writerow(
                [
                    cena["cena"]
                ]
            )

def shrani_artikle3(ime_dat, seznam_slovarjev3):
    with open(ime_dat, "w", encoding='UTF-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "lokacija"
            ]
        )

        for lokacija in seznam_slovarjev3:
            pisatelj.writerow(
                [
                    lokacija["lokacija"]
                ]
            )

def shrani_artikle4(ime_dat, seznam_slovarjev4):
    with open(ime_dat, "w", encoding='UTF-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "cas",
                "datum"
            ]
        )

        for datum in seznam_slovarjev4:
            pisatelj.writerow(
                [
                    datum["cas"],
                    datum["datum"]
                ]
            )

def shrani_artikle5(ime_dat, seznam_slovarjev5):
    with open(ime_dat, "w", encoding='UTF-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "je_ni_trgovec"
            ]
        )

        for je_ni_trgovec in seznam_slovarjev5:
            pisatelj.writerow(
                [
                    je_ni_trgovec["je_ni_trgovec"]
                ]
            )
