import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)  # return first element of cards (and remove it)

    @property
    def cards(self):
        return self._cards

    def __len__(self):   # called by len(obj)
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}:{len(self)}"

    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

if __name__ == "__main__":
    cd1 = CardDeck()
    print(cd1)
    cd1.shuffle()  # object method
    print(cd1.cards)
    print()
    for i in range(5):
        card = cd1.draw()
        print(card)
    print(len(cd1))
    print(cd1)