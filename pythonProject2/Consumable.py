from Item import Item


class Consumable(Item):
    def __init__(self, position, size, image):
        super().__init__(position, size, image)

    def consume(self, player, scenery):
        pass
