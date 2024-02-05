from Item import Item


class Water(Item):
    def __init__(self, position, size, image):
        super().__init__(position, size, image)
        self.breakable = False


