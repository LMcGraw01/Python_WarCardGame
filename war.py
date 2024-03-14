import random

#setting both player's score to zero
player_one_score = 0
player_two_score = 0

#create empty deck
deck = []

def populate_deck():
    for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
        for rank in range(2,15):
            deck.append((rank,suit))

#defining the card pairs once the value exceeds 10
def printable_card(card):
    if card[0] <= 10: rank = str(card[0])
    if card[0] == 11: rank = "Jack"
    if card[0] == 12: rank = "Queen"
    if card[0] == 13: rank = "King"
    if card[0] == 14: rank = "Ace"
    fullname = rank + " of " + card[1]
    return fullname

#draws card fom stack and prints to screen
def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])    
    print(player + " drew the " + printable_card(card))
    return card

#make the deck
populate_deck()
#shuffle the deck
random.shuffle(deck)


#every turn, 
while True:
    #each player draws card   
    player_one_card = draw_card("Player one")
    player_two_card = draw_card("Player two")
    #compare to see who wins
    if player_one_card[0] > player_two_card[0]: 
        winner = "Player One"
        player_one_score += 2
    elif player_one_card[0] < player_two_card[0]:
        winner = "Player Two"
        player_two_score += 2
    else: winner = "No one"

    print(winner + " wins! ")
    print("\n")
    #tiebreaker


    #keep score
    #check whether the deck is empty 
    if len(deck) == 0:
        print("Game over. Deck is empty")
        print("Player one: " + str(player_one_score))
        print("Player two: " + str(player_two_score))
        break