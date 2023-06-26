import random
from views import PrinterCardView
from cards import PlayingCard

STANDARD_SUITS = ["clubs", "spades", "hearts", "diamonds"]
_emojis = ["\U00002663", "\U00002660", "\U00002665", "\U00002666"]
STANDARD_VALUES = values = (["A"] +
                            [str(v) for v in range(2,11)] +
                            ["J", "Q", "K"])

class PlayingCardGame:
    def __init__(self, card_view_class) -> None:
        deck = self.build_standard_deck(False, card_view_class)
        self.deck = deck
        self.discarded = []
        random.shuffle(self.deck)
        self.running = True

    def build_standard_deck(self, cards_up, view_class):
        deck = []
        for suit in STANDARD_SUITS:
            for value in STANDARD_VALUES:
                card = PlayingCard(value, suit, cards_up)
                view = view_class(card)
                deck.append(view)
        return deck


    def draw(self, view):
        view.draw()

    def run(self):
        n = 1
        while self.running:
            print("-" * 14, f"{n} turno", "-" * 14)
            card = self.deck.pop()
            self.draw(card)
            resp = input("Virar? (S/N)")
            if resp.lower() == "s":
                card.flip()
            self.discarded.append(card)
            if not self.deck:
                self.running == False
            input()
            n += 1
        print("Obrigado por jogar!")

if __name__ == "__main__":
    game = PlayingCardGame(PrinterCardView)
    game.run()
