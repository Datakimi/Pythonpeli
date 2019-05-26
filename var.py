
from enum import Enum
from enum import IntEnum
import random
myList=(["Range" ,"Melee" ,"Mage" ])
kone_choice = (random.choice(myList))
print([kone_choice])
Yeet = {"Yeet": 10}
Skeet = {"Skeet": 20}
Jkeet = {"Jkeet": 30}
peep = {"health": 100}
player = {"2"} #Range
tts = {"3"} #Mage
pps = {"4"} #Melee
myListt=([pps, player, tts ])
choice = (random.choice(myListt))
print (choice)
hyokkays_lista = []
partial_deck = []
Mina_hyok = []
Kone_hyok = []
 #   choice = ["pps"]
#    peep["health"] = peep["health"] - Yeet["Yeet"] 

if  kone_choice == 'Range':
        peep["health"] = peep["health"] - Yeet["Yeet"] 
elif kone_choice == 'Melee':
        peep["health"] = peep["health"] - Skeet["Skeet"] 
elif kone_choice == 'Mage':
        peep["health"] = peep["health"] - Jkeet["Jkeet"] 

    #elif stroke == par - 2:
#        text = 'Eagle!'
 #   elif stroke == par - 1:
  #      text = 'Birdie!'
   # elif stroke == par:
    #    text = 'Par'
#    elif stroke == par + 1:
 #       text = 'Bogey :('
  #  elif stroke == par + 2:
   #     text = 'Double Bogey :('
   # elif stroke == par + 3:
    #    text = 'Triple Bogey :('
   # else:
    #    text = '+ ' + str(stroke - par) + ' :('
#player_choice = input()
    #Komennot vähentää vastustajan terveys pisteet hyökkäys valinnan mukaan
#if player_choice == "1":
            
 #   if choice == [player"2"]:
  #  print("Voitit")
   # peep["health"] = peep["health"] - Yeet["Yeet"] 

   #     else:
    #    print("Hävisit")
                #Jos pelaajan terveys menee 0 kone voittaa


class Card (IntEnum):
    Melee = 10
    Range = 10
    Mage = 10

class Suit(Enum) :
    Melee = 'Melee'
    Range = 'Range'
    Mage = 'Mage'

class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit
        #Funktio joka jakaa kortit
def create_deck():
    for suit in Suit :
        for card in Card:
            hyokkays_lista.append(PlayingCard(Card(card), Suit(suit)))
    return hyokkays_lista
#for i in range(0, len(hyokkays_lista)):
 #   print("Card:", hyokkays_lista[i].card)
  #  print("Suit: ", hyokkays_lista[i].suit)
  #Ottaa yhen kortin
def draw_card(deck):
    rand_card = random.randint(0, len(deck) -1)
    return deck.pop(rand_card)
# Deal two players for the game of war
def deal_war():
    while(len(partial_deck) > 0):
        Mina_hyok.append(draw_card(partial_deck))
        Kone_hyok.append(draw_card(partial_deck))

create_deck()
partial_deck = list(hyokkays_lista)

test_card = draw_card(partial_deck)
print ("You drew a: ", test_card.suit)
deal_war()
        #if kone_choice == ['Mage']:
         #   print("hell yeah")
        #else:
        #    print("YEEEH")
        
for i in range(0, len(Mina_hyok)):
    if (Mina_hyok[i].card > Kone_hyok[i].card):
        print("Voitit pelin ", Mina_hyok[i].card)
        print("Kone hävisi ", Kone_hyok[i].card)
    if(Mina_hyok[i].card < Kone_hyok[i].card):
        print("Kone voitti ", Kone_hyok[i].card)
        print("Hävisit pelin ", Mina_hyok[i].card)
        
    else:
        print("WARRRRRR")

print(peep["health"])
print(Yeet["Yeet"])

#player = {"name": "Kimi", "Melee" : 10, "Mage" : 10, "Range" : 10, "heal" : r1, "health": 100 

