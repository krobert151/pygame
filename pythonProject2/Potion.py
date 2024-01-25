from Object import Object


class Potion(Object):
    def __init__(self, position, size, image, effect):
        super().__init__(position, size, image)
        self.position = position
        self.size = size
        self.image = image
        self.effect = effect
