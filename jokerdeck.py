from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()  # call parent method
        for joker_number in 1, 2:
            joker = Card("JOKER", "JOKER")
            self._cards.append(joker)

if __name__ == "__main__":
    jd = JokerDeck()
    jd.shuffle()
    print(jd.cards)
    print()
    print(jd.draw())
    print(jd)