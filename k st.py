Betyg_värde =  {"A":20, "B":17.5, "C":15,"D":12.5, "E":10, "F":0, "-":0}
Betyg = {"Teknik 1": "A", "Fysik 1" : "D"}
Kurs_poäng = {"Teknik 1": 150, "Fysik 1 ": 150, "Historia 1a": 50}

for x,y in Betyg_värde.items():
    print (x,y)

while True:
    menyval = input("\n1. Kolla betyg\n"
                   "2. Ändra betyg\n"
                   "3. Lägg till betyg\n"
                   "4. Räkna ut meritvärde\n"
                   "5. Avsluta program\n")

    if menyval == "1":
            for kurs, betyg in betyg.items():
                print(f"{kurs} : {betyg}")

    elif menyval == "2":
            Kurs = input("Vilken ämne vill du ändra  ett betyg i? ").capitalize()
            if kurs in betyg:
                betyg[kurs] = input(f" til Vilket betyg vill du ändra till  {kurs}? ").capitalize()
            else:
                print(f"Det finns ej betyg i den här {kurs} just nu.")