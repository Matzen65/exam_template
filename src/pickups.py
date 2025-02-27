import random


class Item:
    """Representerar saker man kan plocka upp."""

    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("Carrot", 20, "C"), Item("Apple", 20, "A"),
           Item("Strawberry", 20, "S"), Item("Cherry", 20, "C"),
           Item("Watermelon", 20, "W"), Item("Radish", 20, "R"),
           Item("Meatball", 30, "M")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

# slumpa en position som är ledig och placera dit en random frukt från pickups
def randomize_extra(grid):
    extra_fruit = random.choice(pickups)
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, extra_fruit)
            return extra_fruit
