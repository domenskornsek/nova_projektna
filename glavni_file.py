import izlusci_podatke
import shrani_podatke
import preberi_podatke


besedila = preberi_podatke.preberi(7)
seznam_slovarjev1 = []
seznam_slovarjev2 = []
seznam_slovarjev3 = []
seznam_slovarjev4 = []
seznam_slovarjev5 = []

for besedilo in besedila:
    bloki = izlusci_podatke.poisci_bloke(besedilo)

    seznam_slovarjev1 += izlusci_podatke.poisci_podatke1(bloki)
    seznam_slovarjev2 += izlusci_podatke.poisci_podatke2(bloki)
    seznam_slovarjev3 += izlusci_podatke.poisci_podatke3(bloki)
    seznam_slovarjev4 += izlusci_podatke.poisci_podatke4(bloki)
    seznam_slovarjev5 += izlusci_podatke.poisci_podatke5(bloki)



shrani_podatke.shrani_artikle1("artikli1.csv", seznam_slovarjev1)
shrani_podatke.shrani_artikle2("artikli2.csv", seznam_slovarjev2)
shrani_podatke.shrani_artikle3("artikli3.csv", seznam_slovarjev3)
shrani_podatke.shrani_artikle4("artikli4.csv", seznam_slovarjev4)
shrani_podatke.shrani_artikle5("artikli5.csv", seznam_slovarjev5)



