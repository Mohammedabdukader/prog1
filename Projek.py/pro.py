import random
spel = ("Hej välkomen till BLackjack! ")
utdelning = ("Utdelaren kommer att dela ut 2 kort sedan får du välja om du vill stanna eller fortsätta")
print(spel)
print (utdelning + "\n")
spela_igen=True
while spela_igen:
    utdelare = []
    spelare1 = []

    for _ in range (2):
        utdelare.append(random.randint(1, 11))
        spelare1.append(random.randint(1, 11))

    print ("utdelare har x &", utdelare[0] )
    print("Du har", spelare1 , "\n")

    if sum(utdelare)<21:
        utdelare.append(random.randint (1, 11))
        
        while sum(spelare1)<= 21 and sum(utdelare) <= 21:
            handling = str (input("vill du stanna eller fortsätta? \n\n")).capitalize()
            if handling == "Stanna":
                while sum(utdelare) < 16:
                    utdelare.append(random.randint (1, 11))
                
                
                print("Du har nu totalt " + str(sum(spelare1)) + " med det här kortet" , spelare1, "\n")
                print ("Utdelaren har totalt "  +  str(sum(utdelare)) + " med här kortet " , utdelare, "\n")

                if sum(utdelare) > sum(spelare1) and sum(utdelare)<=21:
                    print ("Utdelaren har vunnit \n")
                    break
                elif sum(spelare1) > sum(utdelare) and sum(spelare1) <=21:
                    print("Du har vunnit \n")
                    break
            
            
            if sum(utdelare) == sum(spelare1):
                    print ("Ni har lika, Ingen vinner! \n")
                    break

            if handling == "Fortsätta": 
                spelare1.append(random.randint (1, 11))
            

                print("Du har nu totalt " + str(sum(spelare1)) + " från det här kortet" , spelare1)
                sträng = "utdelare har totallt "
                for i in range(len(utdelare)-1):
                    sträng += "x "
                sträng += str(utdelare[0])
                print (sträng + "\n")
            
        

    
    if sum (spelare1) > 21:
            print("Utdelare har", utdelare)
            print ("Du torska! utdelaren vinner. \n")
        
    elif sum (spelare1) ==21: 
            print ("Du har 21! grattis för den stora vinsten")
    spela_igen = input("vill du spela igen? Ja eller Nej! \n").lower()
    if spela_igen =="ja:":
        continue 
    if spela_igen =="nej":
        spela_igen=False
        print ("\n","Ha en bra dag")
    
                

