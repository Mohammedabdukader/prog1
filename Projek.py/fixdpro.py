import random
#spelar_poäng=0
#utdelar_poäng=0
#while spelar_poäng<3 and utdelar_poäng<3: 
spel = ("Hej välkomen till BLackjack! ")
utdelning = ("Utdelaren kommer att dela ut 2 kort sedan får du välja om du vill stanna eller fortsätta")
print(spel)
print (utdelning + "\n")

utdelare = []
spelare1 = []
while len(spelare1) != 2:
    spelare1.append(random.randint(1, 11))
    if len(spelare1) == 2:
while len(utdelare) != 2:
    utdelare.append(random.randint(1, 11))
    if len (utdelare) == 2:
        print ("utdelare har Y &", utdelare[1])

for _ in range (2):
    utdelare.append(random.randint(1, 11))
    spelare1.append(random.randint(1, 11))

print ("utdelare har Y &", utdelare[1])



print("Du har", spelare1 )
while sum(spelare1)< 21:
    handling = str (input("vill du stanna eller fortsätta? ")).capitalize()
    if handling == "Fortsätta": 
        spelare1.append(random.randint (1, 11))

        print ("Utdelaren har totalt "  +  str(sum(utdelare)) + " med här kortet " , utdelare ) 

    elif handling == "Stannar":
        print("Du har totalt " + str(sum(spelare1)) +  " med det här kortet ",  spelare1)
        print("Ut har nu totalt " + str(sum(utdelare)) + " från det här kortet ", utdelare)
        print ("gratis för vinsten")
    break

# Händer efter spelaren har kört
while (sum(utdelare)) <=16:
    utdelare.append (random.randint(1, 11))