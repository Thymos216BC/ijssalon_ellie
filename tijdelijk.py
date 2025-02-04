prijzen = {"aardbei" : 3, "vanille" : 4, "chocolade" : 5}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aandbieding: vanille-ijs, 1 liter - slechts {aanbieding}"
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
el = [str.lower() for str in reclame_tekst4]
for i in el:
    if len(i) >= 5:
        print(i.upper())
    else:
        print(i)