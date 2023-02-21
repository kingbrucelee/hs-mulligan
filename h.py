from tqdm import tqdm # Progress bars
import random 
mulligan = True # True - Losujemy ponownie (raz) karty złe False - Nie 
coin = False # False - Gracz jest pierwszy (3 karty), True - Gracz jest drugi (4 karty + Moneta)
good_cards = ['Jajko','Lokacja']
print("Mulligan")
erw = 0
for i in tqdm(range(0,100000000)):
    hand = list()
    deck = ['Jajko', 'Jajko', 'Lokacja', 'Lokacja','random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit', 'random_shit']
    if mulligan:
        if coin:
            for i in range(0,4):
                card = random.choice(deck)
                if card in good_cards:
                    hand.append(card)
                    deck.remove(card)
                else:
                    card = random.choice(deck)
                    hand.append(card)
                    deck.remove(card)
            hand.append("Moneta") 
        else:
            for i in range(0,3):
                card = random.choice(deck)
                if card in good_cards:
                    hand.append(card)
                    deck.remove(card)
                else:
                    card = random.choice(deck)
                    hand.append(card)
                    deck.remove(card) 
    else:
        if coin:
            for i in range(0,4):
                card = random.choice(deck)
                hand.append(card)
                deck.remove(card)
            hand.append("Moneta") 
        else:
            for i in range(0,3):
                card = random.choice(deck)
                hand.append(card)
                deck.remove(card)
    if good_cards[0] in hand and good_cards[1] in hand:
        erw+=1
print(erw)