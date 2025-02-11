mijn_dict = {'vis':10,
             'vlees':25,
             'overig':15}
totaal = 50

def presenteer(dictionary,totaal):
    uitvoer = []
    for key,value in dictionary.items():
        uitvoer.append(f"{key} : {value} euro")
    uitvoer.append("="*26)
    uitvoer.append(f"totaal : {totaal} euro")
    for el in uitvoer:
        print(el)