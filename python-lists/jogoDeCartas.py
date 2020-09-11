import random 
print('Challenge 1')
print('Randomly choose five cards to add to a players hand')
print('HMAP')
print('Dealing.....')

cards = []
n = 0

while len(cards) < 52:
    n = n + 1
    cards.append(n)
tam = len(cards)
print('There are {} in the deck.'.format(tam))

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

n = 0

while n < 5:
    n = n + 1
    card = random.choice(cards)
    cards.remove(card)
    suit = random.choice(suits)
    print(f'Card number {card} and card name {suit}')

tam = len(cards)
print('Left {} cards on the deck.'.format(tam))
print('Finished.')