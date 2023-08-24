import re

def poisci_bloke(besedilo):
    bloki = []
    vzorec_bloka = re.compile(
        r'<article class="entity-body cf">' r".*?" r"</ul>\s+</div>\s+</article>",
        flags=re.DOTALL,
    )

    for najdba in vzorec_bloka.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])
    
    #print(bloki)

    return bloki


#def izlusci_podatke_iz_blokov(bloki):
#    podatki_artiklov = []
#    for blok in bloki:
#        podatki_artiklov.append(izlusci_podatke(blok))
#    return podatki_artiklov

#def poisci_podatke(bloki):
#    seznam_slovarjev = []  # Create an empty list to store dictionaries
#    
#    # Compile the regular expressions
#    vzorec_stevilka_link_naslov = re.compile(r'<h3 class="entity-title"><a name="(?P<stevilka>\d+)" class="link" href="(?P<link>.+)">(?P<naslov_izdelka>.+)</a></h3>')
#    vzorec_cena = re.compile(r'<strong class="price price--hrk">\s*(?P<cena>\d+)')
#    vzorec_lokacija = re.compile(r'<span class="entity-description-itemCaption">Lokacija: </span>(?P<lokacija>.+)<br />')
#    vzorec_datum = re.compile(r'<time class="date date--full" datetime="(?P<cas>.+)" pubdate="pubdate">(?P<datum>.+)</time>')
#    vzorec_je_ni_trgovec = re.compile(r'<span class="icon-item feature feature--User".+>(?P<je_ni_trgovec>.+)</span>')
#    
#    for blok in bloki:
#        slovar = {}
#        najdba1 = vzorec_stevilka_link_naslov.search(blok)
#        najdba2 = vzorec_cena.search(blok)
#        najdba3 = vzorec_lokacija.search(blok)
#        najdba4 = vzorec_datum.search(blok)
#        najdba5 = vzorec_je_ni_trgovec.search(blok)
#        
#        if najdba1:
#            slovar["stevilka"] = int(najdba1["stevilka"])
#            slovar["link"] = najdba1["link"]
#            slovar["naslov_izdelka"] = najdba1["naslov_izdelka"]
#
#        if najdba2:
#            slovar["cena"] = int(najdba2["cena"])
#        
#        if najdba3:
#            slovar["lokacija"] = najdba3["lokacija"]
#        
#        if najdba4:
#            slovar["cas"] = najdba4["cas"]
#            slovar["datum"] = najdba4["datum"]
#        
#        if najdba5:
#            slovar["je_ni_trgovec"] = najdba5["je_ni_trgovec"]
#        
#        seznam_slovarjev.append(slovar)  # Append the dictionary to the list
#    
#    return seznam_slovarjev  # Return the list of dictionaries
#
## Sample HTML blocks
#html_blocks = [
#    '<article class="entity-body cf">\n\n    \n                    <h3 class="entity-title"><a name="4509629" class="link" href="/oprema-za-bazene/pokrov-bazen-oglas-4509629">Pokrov za bazen INTEX</a></h3>\n        \n                    <div class="entity-thumbnail">\n                <a class="link" href="/oprema-za-bazene/pokrov-bazen-oglas-4509629">\n                    <img\n                        class="img entity-thumbnail-img"\n                        src="https://static.bolha.com/dist/ceb7cc1a7b.png"\n                        data-src="//www.bolha.com/image-200x150/oprema-za-bazene/pokrov-bazen-slika-18691793.jpg"\n                        alt="Pokrov za bazen INTEX"\n                    />\n                    <noscript>\n                        <img\n                       class="img entity-thumbnail-img"\n                            src="//www.bolha.com/image-200x150/oprema-za-bazene/pokrov-bazen-slika-18691793.jpg"\n                            alt="Pokrov za bazen INTEX"\n                        />\n                    </noscript>\n                    <div class="entity-thumbnail-preloader">\n                        <div class="Preloader Preloader--center">\n                            <div class="Preloader-inner"></div>\n                        </div>\n                    </div>\n                </a>\n            </div>\n        \n        \n                    <div class="entity-description">\n                                    <div class="entity-description-main">\n                                        <span class="entity-description-itemCaption">Lokacija: </span>Vrhnika, Vrhnika<br />\n                                                           </div>\n                \n            </div>\n        \n                    <div class="entity-pub-date">\n                <span class="label">Objavljen:</span>\n              <time class="date date--full" datetime="2023-08-21T08:40:56+02:00" pubdate="pubdate">21.08.2023.</time>\n            </div>\n        \n        \n                    <div class="entity-notice entity-notice--saved-ad notice-ad-saved  hidden ">\n                            </div>\n        \n        \n                    <div class="entity-tools">\n                <ul class="tool-items">\n\n                                            <li class="tool-item">\n                            <button class="icon-item tool tool--SaveAd js-veza-save_ad " type="button" title="Shrani oglas"><span class="icon icon--action icon--xs icon--save-item">Shrani oglas</span></button>\n                        </li>\n                    \n                    \n          \n                </ul>\n            </div>\n        \n                    <div class="entity-features">\n                <ul class="feature-items cf">\n\n                    \n                                            <li class="feature-item">\n                            <button class="icon-item feature feature--Map js-faux-anchor" type="button" data-href="/oprema-za-bazene/pokrov-bazen-oglas-4509629?tab=map" title="Ta oglas je umeščen na zemljevidu"><span class="icon icon--action icon--s icon--map">Prikaži na zemljevidu</span></button>\n         </li>\n                    \n                    \n                    \n                    \n                    \n                    \n                                   <li class="feature-item">\n                            <span class="icon-item feature feature--User" title="Uporabnik ni trgovec"><span class="icon icon--action icon--s icon--user">Uporabnik ni trgovec</span></span>\n                        </li>\n                                            \n                                    </ul>\n            </div>\n        \n        \n                    <div class="entity-prices">\n                <ul class="price-items cf">\n                                            <li class="price-item">\n                            <strong class="price price--hrk">\n                                10&nbsp;<span class="currency">€</span>                            </strong>\n          </li>\n                                                            </ul>\n            </div>\n        \n        \n        \n    \n</article>',
#    # ... Add more HTML blocks here ...
#]
#
## Process the HTML blocks
#slovarji = poisci_podatke(html_blocks)
#
## Print the extracted data
#for slovar in slovarji:
#    print(slovar)


def poisci_podatke1(bloki):
    seznam_slovarjev1 = []  # Create an empty list to store dictionaries

    for blok in bloki:
        slovar = {}
        vzorec_stevilka_link_naslov = re.compile(r'<h3 class="entity-title"><a name="(?P<stevilka>\d+)" class="link" href="(?P<link>.+)">(?P<naslov_izdelka>.+)</a></h3>')
        najdba = vzorec_stevilka_link_naslov.search(blok)
        
        if najdba is not None:
            slovar["stevilka"] = int(najdba["stevilka"])
            slovar["link"] = najdba["link"]
            slovar["naslov_izdelka"] = najdba["naslov_izdelka"]
            seznam_slovarjev1.append(slovar)  # Append the dictionary to the list
    
    return seznam_slovarjev1  # Return the list of dictionaries

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
