import re

def poisci_bloke(besedilo):
    bloki = []
    vzorec_bloka = re.compile(
        r'<article class="entity-body cf">' r".*?" r"</ul>\s+</div>\s+</article>",
        flags=re.DOTALL,
    )

    for najdba in vzorec_bloka.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])
    
    return bloki


def poisci_podatke1(bloki):
    seznam_slovarjev1 = []

    for blok in bloki:
        slovar = {}
        vzorec_stevilka_link_naslov = re.compile(r'<h3 class="entity-title"><a name="(?P<stevilka>\d+)" class="link" href="(?P<link>.+)">(?P<naslov_izdelka>.+)</a></h3>')
        najdba = vzorec_stevilka_link_naslov.search(blok)
        
        if najdba is not None:
            slovar["stevilka"] = int(najdba["stevilka"])
            slovar["link"] = najdba["link"]
            slovar["naslov_izdelka"] = najdba["naslov_izdelka"]
            seznam_slovarjev1.append(slovar)  
    
    return seznam_slovarjev1  

def poisci_podatke2(bloki):
    seznam_slovarjev2 = []

    for blok in bloki:
        slovar = {}
        vzorec_cena = re.compile(r'<strong class="price price--hrk">\s*(?P<cena>\d+)')
        najdba = vzorec_cena.search(blok)
        
        if najdba is not None:
            slovar["cena"] = int(najdba["cena"])
            seznam_slovarjev2.append(slovar)
    
    return seznam_slovarjev2

def poisci_podatke3(bloki):
    seznam_slovarjev3 = []

    for blok in bloki:
        slovar = {}
        vzorec_lokacija = re.compile(r'<span class="entity-description-itemCaption">Lokacija: </span>(?P<lokacija>.+)<br />')

        najdba = vzorec_lokacija.search(blok)
        
        if najdba is not None:
            slovar["lokacija"] = najdba["lokacija"]
            seznam_slovarjev3.append(slovar)
    
    return seznam_slovarjev3

def poisci_podatke4(bloki):
    seznam_slovarjev4 = []

    for blok in bloki:
        slovar = {}
        vzorec_datum = re.compile(r'<time class="date date--full" datetime="(?P<cas>.+)" pubdate="pubdate">(?P<datum>.+)</time>')

        najdba = vzorec_datum.search(blok)
        
        if najdba is not None:
            slovar["cas"] = najdba["cas"]
            slovar["datum"] = najdba["datum"]
            seznam_slovarjev4.append(slovar)
    
    return seznam_slovarjev4

def poisci_podatke5(bloki):
    seznam_slovarjev5 = []

    for blok in bloki:
        slovar = {}
        vzorec_je_ni_trgovec = re.compile(r'<span class="icon-item feature feature--User" title="Uporabnik ni trgovec"><span class="icon icon--action icon--s icon--user">(?P<je_ni_trgovec>.+)</span></span>')

        najdba = vzorec_je_ni_trgovec.search(blok)
        
        if najdba is not None:
            slovar["je_ni_trgovec"] = najdba["je_ni_trgovec"]
            seznam_slovarjev5.append(slovar)
    
    return seznam_slovarjev5
