from PIL import Image

IMG_DIR = "img"

class CardView:
    def __init__(self, card) -> None:
        self.card = card

    def flip(self):
        self.card.flip()
        self.draw()

    def draw(self):
        raise NotImplementedError()


class PrinterCardView(CardView):
    def draw(self):
        if self.card.face_up:
            print(self.card)
        else:
            print("\U0001F3B4")

class ImageCardView(CardView):
    pass
