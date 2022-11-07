# Loginmeny
# Skelettkod till uppgiften



accounts = {"hampus1" : "hampus123"}
logged_in = False

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":
        print ("skapa ett ett konto")
        username= input("Username:" )
        Lösenord = input("Lösenord:" )
        accounts [username] = Lösenord
        print (accounts)
       

    elif menyval == "2":
        försök = 0
        if försök <= 3:
        
            print ("logga in")
            username_try = input ("Username: ")
            Lösenord_try = input("Lösenord: ")

            
            if username_try in accounts: 
                if accounts[username_try]== Lösenord_try:
                    logged_in = True
                    print ("Inloggad")
                    försök + 1

                
            if logged_in== False: 
                print ("skriv rätt lösenord och rätt username")
                försök + 1 
            


    elif menyval == "3":
        if logged_in == True: 
            print ("skriv någoit roligt")

    elif menyval == "4":
        säker = input ("Är du säker på att du vill logga ut, det var jätte kul och ha dig här: ").capitalize()
        if säker == "Yes":
            print ("Du är utloggad:")
            logged_in = False
           


  

    elif menyval == "5":
        break