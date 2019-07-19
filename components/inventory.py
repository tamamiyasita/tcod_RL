import tcod as libtcod

from game_messages import Message


class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                "item_added": None,
                "message": Message("you cannot carry any more, inventory is full", libtcod.yellow)
            })
        else:
            results.append({
                "item_added": item,
                "message": Message("you pick up the {0}!".format(item.name), libtcod.blue)
            })

            self.items.append(item)

        return results