from Object import Object


class BackPack(Object):

    def __init__(self, position, size, image):
        super().__init__(position, size, image)
        self.equipped = False
        self.items = {}
        self.capacity = 10
        self.size = size
        self.position = position
        self.image = image

    def add_item(self, item):
        if isinstance(item, Object):
            if item not in self.items:
                self.items[item] = 1
            else:
                self.items[item] += 1
            return True
        return False

    def consume_item_by_index(self, index):
        items_list = list(self.items.keys())
        if 0 <= index < len(items_list):
            consumed_item = items_list[index]
            if self.consume_item(consumed_item):

                # Implement your logic for consuming the item (e.g., incrementing player stats, etc.)
                print(f"Consumed item: {consumed_item}")
        else:
            print("Invalid index")

    def consume_item(self, item):
        if item in self.items and self.items[item] > 0:
            self.items[item] -= 1
            if self.items[item] == 0:
                self.items.pop(item)
            # Implement your logic for consuming the item (e.g., incrementing player stats, etc.)
            print(f"Consumed item: {item}")
            return True
        else:
            print("Item not found or no more left.")
            return False