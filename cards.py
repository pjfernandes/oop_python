STANDARD_SUITS = ["clubs", "spades", "hearts", "diamonds"]
_emojis = ["\U00002663", "\U00002660", "\U00002665", "\U00002666"]
STANDARD_VALUES = values = (["A"] +
                            [str(v) for v in range(2,11)] +
                            ["J", "Q", "K"])

EMOJI_MAP = dict(zip(STANDARD_SUITS, _emojis))

class PlayingCard:
    def __init__(self, value, suit, up=True) -> None:
        self.value = value
        self.suit = suit
        self.face_up = up

    def flip(self):
        self.face_up = not self.face_up

    def __str__(self) -> str:
        return f"{self.value}{EMOJI_MAP[self.suit]}"

if __name__ == '__main__':
    card = PlayingCard(7, STANDARD_SUITS[2])
    print(card)
