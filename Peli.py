#Tämän moduulin avulla saan random komennot mukaan
import random
#Komento pitää pelin päällä että peli ei suoraan sulje itseänsä kun sen avaa
game_running = True
while game_running == True:
    new_round = True
    #Laaditaan pelaajan ja koneen nimi, hyökkäykset, parannus, terveys.
    player = {"name": "Kimi", "Melee" : 10, "Mage" : 10, "Range" : 10, "health": 100 }
    Kone = {"name": "Kone", "Melee" : 10, "Mage" : 10, "Range" : 10, "health": 100 }
    
    while new_round == True:
    #Näillä 2 booleanilla tehdään ohjelman aikana niin että kun esim. player_won = True peli loppuu, että terveys ei voi mennä miinukselle
        player_won = False
        kone_won = False
        #Tällä listalla kone tekee valinnan minkä hyökkäyksen se valitsee
        myList=(["Range","Melee","Mage"])
        kone_choice = (random.choice(myList))

        #Tämä komento valitsee yhden numeron 1,20 väliltä
        heal = random.randint(1,20) 
        #tulostaa koneen valinnan
        print("Kone valitsi", kone_choice, "hyökkäyksen")
    #tulostaa pelaajan ja koneen nimen
        print(player["name"])
        print(Kone["name"])
    #Tulostaa pelaajan ja koneen terveyspisteet
        print(player["health"])
        print(Kone["health"])
        #Kertoo pelaajalle hyökkäys vaihtoehdot
        print("Please select action")
        print("1) Melee")
        print("2) Mage")
        print("3) Range")
        print("4) Heal")
        print("5) Exit Game")
    #Antaa pelaajalle mahdollisuuden laittaa vastauksen terminaaliin
        player_choice = input()
    #Komennot vähentää vastustajan ja pelaajan terveys pisteet hyökkäys valinnan mukaan
        if player_choice == "1":
            if kone_choice == "Mage":
                player["health"] = player["health"] - Kone["Mage"] 
            elif kone_choice == "Melee":
                player["health"] = player["health"] - Kone["Melee"] 
                Kone["health"] = Kone["health"] - player["Melee"] 
            elif kone_choice == "Range":
                Kone["health"] = Kone["health"] - player["Melee"]           
            #Jos koneen terveys menee 0 pelaaja voittaa
            if Kone["health"] <= 0:
                    player_won = True
                    #Tulostaa ruutuun jos voitit
                    print("Voitit!")
            else:
                
                #Jos pelaajan terveys menee 0 kone voittaa
                if player["health"] <=  0:
                    kone_won = True
                    #Tulostaa ruutuun jos hävisit
                    print("Hävisit!")

        elif player_choice == "2":
            if kone_choice == "Range":
                player["health"] = player["health"] - Kone["Range"] 
            elif kone_choice == "Mage":
                player["health"] = player["health"] - Kone["Mage"] 
                Kone["health"] = Kone["health"] - player["Mage"]
            elif kone_choice == "Melee":
                Kone["health"] = Kone["health"] - player["Melee"]
            if Kone["health"] <= 0:
                player_won = True
                print("Voitit!")
            else:
                if player["health"] <=  0:
                    kone_won = True
                    print("Hävisit!") 

        elif player_choice == "3":
            if kone_choice == "Melee":
                player["health"] = player["health"] - Kone["Melee"] 
            elif kone_choice == "Range":
                player["health"] = player["health"] - Kone["Range"] 
                Kone["health"] = Kone["health"] - player["Range"]
            elif kone_choice == "Mage":
                Kone["health"] = Kone["health"] - player["Range"]
            if Kone["health"] <= 0:
                player_won = True
                print("Voitit!")
            else:
                if player["health"] <=  0:
                    kone_won = True 
                    print("Hävisit!")
            
        elif player_choice == "4":
            #Parantaa pelaajan 1-20 väliltä mutta tekee silti koneen vahingon.
            player["health"] = player["health"] + heal
            player["health"] = player["health"] - Kone["Range"] 
            #tulostaa paljon pelaaja paransi
            print("Parannuit", heal, "parannuspisteellä")
            if Kone["health"] <= 0:
                player_won = True
                print("Voitit!")
            else:
                if player["health"] <=  0:
                    kone_won = True 
                    print("Hävisit!")
            #Lopettaa pelin
        elif player_choice == "5":
            new_round = False
            game_running = False
        else:
            #kertoo pelaajalle jos oli laittanut väärän vaihtoehdon, eli jos laitto jonkuin muun kuin (1,2,3,4,5)
            print("invalid input")
        #Laatii sen jos pelaaja tai kone voittaa, peli loppuu.
        if player_won == True or kone_won == True:    
                new_round = False