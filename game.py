import random
r1 = random.randint(1,30) 
myList=(["Range","Melee","Mage"])
print(random.choice(myList))
Kone_choice = myList
#Komento pitää pelin päällä että peli ei suoraan sulje itseänsä kun sen avaa
game_running = True
while game_running == True:
    new_round = True
    #Laaditaan pelaajan ja koneen nimi, hyökkäys, parannus, terveys.
    player = {"name": "Kimi", "Melee" : 10, "Mage" : 10, "Range" : 10, "heal" : r1, "health": 100 }
    Kone = {"name": "Kone", "Melee" : 10, "Mage" : 10, "Range" : 10, "heal": r1, "health": 100 }
    
    while new_round == True:

    #Näillä 2 booleanilla tehdään ohjelman aikana niin että kun esim. player_won = True peli loppuu, että terveys ei voi mennä miinukselle
        player_won = False
        kone_won = False

    #tulostaa pelaajan ja koneen nimen
        print(player["name"])
        print(Kone["name"])
        #Kertoo pelaajalle minkä hyökkäyksen valitsee
        print("Please select action")
        print("1) Melee")
        print("2) Mage")
        print("3) Range")
        print("4) Heal")
        print("5) Exit Game")
    #Antaa pelaajalle mahdollisuuden laittaa vastauksen terminaaliin
        player_choice = input()
    #Komennot vähentää vastustajan terveys pisteet hyökkäys valinnan mukaan
        if player_choice == "1":
            Kone["health"] = Kone["health"] - player["Melee"]
            #Jos koneen terveys menee 0 pelaaja voittaa
            if Kone["health"] <= 0:
                player_won = True

            else:
                player["health"] = player["health"] - Kone["Melee"] 
                #Jos pelaajan terveys menee 0 kone voittaa
                if player["health"] <=  0:
                    kone_won = True
#        if player_choice == "2":
#            If Kone_choice = Kone["Range"]
 #               player["health"] = player["health"] - Kone["Range"] 
  #          If Kone_choice = Kone["Mage"]
   #             player["health"] = player["health"] - Kone["Mage"] 
    #            Kone["health"] = Kone["health"] - player["Mage"]
     #       If Kone_choice = Kone["Melee"]
      #          Kone["health"] = Kone["health"] - player["Melee"]
    #Tulostaa peelaajan ja koneen terveyspisteet
            print(player["health"])
            print(Kone["health"])
            
        #  print(Kone["health"])
        elif player_choice == "4":
             player["health"] + player["heal"] 
            
        elif player_choice == "5":
            new_round = False
            game_running = False
        else:
            #kertoo pelaajalle jos oli laittanut väärän vaihto-ehdon, eli jos laitto jonkuin muun kuin (1,2)
            print("invalid input")
        #Laatii sen jos pelaaja tai kone voittaa, peli loppuu.
        if player_won == True or kone_won == True:    
                new_round = False