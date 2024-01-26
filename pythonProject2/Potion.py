from Consumable import Consumable


class Potion(Consumable):
    def consume(self, player, scenery):
        super().consume(player, scenery)
        if self.effect.__contains__('HP'):
            number = str(self.effect).removeprefix('HP(')
            number = number.removesuffix(')')
            player.live_bar += int(number)
        elif self.effect.__contains__('O'):
            player.breath = 300

    def __init__(self, position, size, image, effect):
        super().__init__(position, size, image)
        self.position = position
        self.size = size
        self.image = image
        self.effect = effect
