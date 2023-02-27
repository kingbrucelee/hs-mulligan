from tqdm import tqdm # Progress bars
import random 
# TODO: Symulować prawdobieństwa turowe (prawdopodobnie konieczne będzie podzielenie na funkcje) 
# Possible Refactor: Zamiast losować za każdym razem i usuwać z talli, przetasować raz talię i pobierać po kolei elementy
mulligan = bool(input("Podaj 1 jeśli chcesz mulligan, 0 jeśli nie \n")) # True - Losujemy ponownie (raz) karty które są złe False - Nie 
try:
    cards_to_draw = int(input("Ile kart ma gracz na starcie otrzymać? \n (Zazwyczaj gracz który wygrywa rzut monetą dostaje 3 a przegrywający 4) \n"))
except ValueError:
    print("Podano znak inny niż liczba. Ustalam ilość kart na 3")
    cards_to_draw = 3    
deck = list()    
good_cards = list()
while True:
    t = input("Wpisuj karty które chcesz otrzymać na ręce startowej jedna per linijka; wpisz 0 by zakończyć \n")
    if t=="0":
        break
    good_cards.append(t)
for g in set(good_cards):
    try:
        deck+= [g] * int(input(f"Ile karty {g} jest w decku? \n"))
    except ValueError:
        print("Podano znak inny niż liczba. Przyjmuje że znajdują się dwie sztuki tej karty")
        deck+= [g] * 2
try:
    dick_size = int(input("Podaj wielkość talii \n"))
except ValueError:
    print("Podano znak inny niż liczba. Ustalam wielkość talii na 30")
    dick_size = 30

deck+= ["random_shit"] * (dick_size-len(good_cards)) # Tworzę talię z dobrych kart i dopełniam losową stałą wartością
starting_deck = deck[:
]
print("Mulligan")
erw = 0

try:
    tests = int(input("Podaj ilość testów (rekomendowane 1 000 000) \n"))
except ValueError:
    print("Podano znak inny niż liczba. Ustalam ilość testów na 1 000 000 \n")
    tests = 1000000

print(f"Twój rozmiar talii to {dick_size}")
print(f"Mulligan {mulligan} ")
print(f"Dobieramy {cards_to_draw} na starcie")  
print(f"Twój rozmiar talii to {dick_size}")
print(f"Karty które chcesz otrzymać to {good_cards} ")
print(f"Ilość testów do przeprowadzenia {tests} ")  
for i in tqdm(range(0,tests)):
    hand = list()
    deck = starting_deck[:]
    for i in range(0,cards_to_draw):
        card = random.choice(deck)
        if mulligan and card not in good_cards:
            card = random.choice(deck)
        hand.append(card)
        deck.remove(card)
    #print(f"Ręka {hand} ")
    if all(good_cards.count(c) <= hand.count(c) for c in set(good_cards)):
        erw+=1
print(erw)