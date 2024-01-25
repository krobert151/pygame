from Object import Object


class Wall(Object):
    def __init__(self, position, size, image):
        super().__init__(position, size, image)
        self.position = position
        self.size = [20, 20]
        self.image = image


