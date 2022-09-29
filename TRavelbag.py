
# Travelbag
# Skelettkod till uppgiften

travelbag = ["vattenflaska", "kläder", "Mobil", "Pengar"]


while True:
     menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg saker i resväskan\n"
                   "3. Ta bort en sak i resväskan\n"
                   "4. Avsluta program\n")

     if menyval == ("1"):
          print (f"Sakerna i väskan är: 2", end="")
          print(*travelbag, sep=", ")
     elif menyval == "2":
          inventory=input("Vad vill du lägga för saker i vätskan?")
          travelbag.append(inventory)
     elif menyval == "3":
          inventory=input("Vad vill du lägga för saker i vätskan?")
          travelbag.remove (inventory)

     elif menyval == "4":
          break
     
     #Tupel = Parentes 
     #List = []
       


