#importera modulen för att göra generera ett utvalt nummer 
import random
#Printa ut en text som förklarar spelet 
spel = ("Hej välkomen till BLackjack! ")
utdelning = ("Utdelaren kommer att dela ut 2 kort sedan får du välja om du vill stanna eller fortsätta")
print(spel)
print (utdelning + "\n")
spela_igen=True
#det ska loopas 
while spela_igen:
    utdelare = []
    spelare1 = []

#ger kort till båda spelarna 
    for _ in range (2):
        utdelare.append(random.randint(1, 11))
        spelare1.append(random.randint(1, 11))

#printa vad utdelader och spelare1 har för kort 
    print ("utdelare har x &", utdelare[0] )
    print("Du har", spelare1 , "\n")
#Kolla summan och om den är mindre än 21 plocka upp en random kort om du vill  
    if sum(utdelare)<21:
        utdelare.append(random.randint (1, 11))

        #Kolla summan av korten så att den är mindre eller lika med båda spelarna 
        while sum(spelare1)<= 21 and sum(utdelare) <= 21:
              #Fråga spelare1 om hen vill plocka upp en till kort  
            handling = str (input("vill du stanna eller fortsätta? \n")).capitalize()

            #definera om handlingen är stanna 
            if handling == "Stanna":
                #om båda korten som utdelaren har är mindre än 16 
                while sum(utdelare) < 16:
                    #plocka upp en till random kort mellan (1, 11)
                    utdelare.append(random.randint (1, 11))
                
                #Printa vad utdelaren och spelare1 har för kort 
                print("Du har nu totalt " + str(sum(spelare1)) + " med det här kortet" , spelare1, "\n")
                print ("Utdelaren har totalt "  +  str(sum(utdelare)) + " med här kortet " , utdelare, "\n")
                #om utdelarens kort är > spelare1 och summan av utdelaren är >=21
                if sum(utdelare) > sum(spelare1) and sum(utdelare)<=21:
                    #print ut att utdelaren vinner  
                    print ("Utdelaren har vunnit \n")
                    #stoppa 
                    break
#ett annat alternativ om summan av kortet i spelare1s händer är > utdelaren och summan av spelare1s är <=21
                elif sum(spelare1) > sum(utdelare) and sum(spelare1) <=21:
                    #Skriv ut att du har vunnit alltså spelare1 då
                    print("Du har vunnit \n")
                    #stoppa 
                    break

            #jämför om spelare1 och utdelare har lika stora kort  
            if sum(utdelare) == sum(spelare1):
                #print ut att de har lika ifall påstående här ovan stämmer 
                    print ("Ni har lika, Ingen vinner! \n")
                    break
            #dfinera handlingen
            if handling == "Fortsätta": 
                #ifall deär fortsätt plocka upp till kort 
                spelare1.append(random.randint (1, 11))
            
            #Skriv ut summan av alla kort 
                print("Du har nu totalt " + str(sum(spelare1)) + " från det här kortet" , spelare1)
                sträng = "utdelare har totallt "
                #Visa bara ett kort från utdelaren även när han plockar upp en till kort 
                for i in range(len(utdelare)-1):
                    sträng += "x "
                sträng += str(utdelare[0])
                print (sträng + "\n")  
   
   
   #om summan av spelare1 > 21 
    if sum (spelare1) > 21:
        #Skriv ut summan av utdelarens kort och därefter printa Vem som vann  
            print("Utdelare har", utdelare)
            print ("Du torska! utdelaren vinner. \n")
    #jämmför summan av spelare1 är 21 och i så fall printa "att du har vunnit med 21"
    elif sum (spelare1) ==21: 
            print ("Du har 21! grattis för den stora vinsten")
    #Definera spela igen och fråga om spelaren vill spela igen  
    spela_igen = input("vill du spela igen? Ja eller Nej! \n").lower()
#Om svaret är ja, fortsätt spelet annars bryt 
    if spela_igen =="ja:":
        continue 
    if spela_igen =="nej":
        spela_igen=False
        print ("\n","Ha en bra dag!")
    
                
