import random

class Grid:
    # class Grid
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig yttre vägg
    block_wall = "O"   # Tecken för en vägg som kan förstöras
    trap = ","
    spade = "#"
    key = "P"
    treasure = "¤"

    #player = "@"

    def __init__(self):
        """Skapa ett "objekt" av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension"
        # för att sätta tecknet för "empty" = ".", på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa oförstörbara väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    def make_block_walls(self):
        """skapar förstörbara väggar inne i spelplanen"""
        self.set(6, 2, self.block_wall)
        self.set(11, 2, self.block_wall)
        for x in range(20, 35):             # vägg nr 1 x-led
            self.set(x, 2, self.block_wall)
        for x in range(4, 12):              # vägg nr 2 x-led
            self.set(x, 3, self.block_wall)
        for x in range(2, 12):
            self.set(x, 1, self.block_wall)
        for x in range(4, 12):
            self.set(x, 4, self.block_wall)

        for y in range(1, 8):              # vägg nr 3 y-leda
            self.set(1, y, self.block_wall)
        for y in range(3, 8):               # vägg nr 4 y-led
            self.set(3, y, self.block_wall)
        for y in range(3, 10):               # vägg nr 4 y-led
            self.set(34, y, self.block_wall)
            self.set(32, y, self.block_wall)

        """ skapar öppningar i väggarna """
        self.clear(3,2)    #se funktion rad 31 ovan
        #self.clear(28, 3)
        #self.set(10, 4, self.empty)
        #self.set(28, 3, self.empty)

        """ skapar en fälla inne på spelplanen"""
    def make_trap(self):
        for y in range(3, 8):
            self.set(2,y, self.trap)
        self.set(33, 5, self.trap)

    def make_spade(self):
        self.set(33, 4, self.spade)
        self.set(4, 5, self.spade)

        """ skapar 2 fast placerade nycklar och 3 skattkistor inne på spelplanen """
         # En tredje nyckel slumpas också ut någonstans på spelplanen
    def make_key(self):
        self.set(33, 1, self.key)
        self.set(8, 2, self.key)
        while True:
            x = self.get_random_x()
            y = self.get_random_y()
            if self.is_empty(x, y):
                self.set(x, y, self.key)
                return False

    def make_treasure(self):
        self.set(4, 2, self.treasure)
        self.set(33, 3, self.treasure)
        self.set(3, 9, self.treasure)

    # Används i filen pickups.pyw
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

