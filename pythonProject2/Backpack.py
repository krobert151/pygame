from Object import Object


class BackPack(Object):

    def __init__(self, position, size, image):
        super().__init__(position, size, image)
        self.equipped = False
        self.items = []
        self.capacity = 10
        self.size = size
        self.position = position
        self.image = image
