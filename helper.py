def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * '*')
    print(f'* {tekst} *')
    print(lengte * '*')
    print()

def fooi_pp(bedrag,personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    uitvoer = f"Het bedrag per persoon is {bedrag_pp} euro."
