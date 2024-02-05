from Item import Item


class Wall(Item):
    def __init__(self, position, size, image, breakable):
        super().__init__(position, size, image)
        self.position = position
        self.size = [20, 20]
        self.image = image
        self.breakable = breakable


