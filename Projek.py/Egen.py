
kortlek = []
färg = ["Hjärter","b    ","c"]
nr = ["Ess", "2", "3", "4"]

for l in färg:
    for n in nr:
        kortlek.append(l + " " + n)

print(stuff)


while True:
     menyval = input("1. Kolla i resväskan\n"
                   "2. vill du ha mer kort\n"
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