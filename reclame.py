from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs*(1-korting)
    uitvoer = f"Vaandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
inkomsten_week = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal*btw
    uitvoer = f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer
def laag_en_hoog(mijn_lijst):
    uitvoer_lijst = []
    uitvoer_lijst.append(min(mijn_lijst))
    uitvoer_lijst.append(max(mijn_lijst))
    return uitvoer_lijst
def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst)/len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer
invoer_lijst = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])
print(combinatie(invoer_lijst))