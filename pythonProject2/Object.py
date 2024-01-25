class Object:
    def __init__(self, position, size, image):
        self.position = position
        self.size = size
        self.image = image

    def hide(self):
        self.position = [-100, -100]