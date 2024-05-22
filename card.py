# data elements: rank suit
class Card:   #  inherits from 'object'
    def __init__(self, rank, suit):
        self._rank  = rank   # private variable
        self._suit = suit

    @property   #  public variable
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    # human-readable info
    def __str__(self):
        return f"Card:{self.rank}-{self.suit}"
    
    # how to reproduce the object
    def __repr__(self):
        # Card(...)
        return f"Card('{self.rank}', '{self.suit}')"
        

if __name__ == "__main__":
    c1 = Card('2', 'Diamonds')
    c2 = Card('Q', 'Spades')
    print(f"{c1.rank = }")
    print(f"{c2.suit = }")
    print(f"{c1 = }")
    print(c1)
    print(c2)
    
