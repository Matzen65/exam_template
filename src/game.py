from .grid import Grid
from .player import Player
from . import pickups

player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1, 0, g):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        #maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)
        score -= 1 # golvet är lava man förlorar ett poäng per steg
    elif command == "s" and player.can_move(0, 1, g):  # move down
        #maybe_item = g.get(player.pos_x, player.pos_y + 1)
        player.move(0, 1)
        score -= 1
    elif command == "w" and player.can_move(0, -1, g):  # move up
        #maybe_item = g.get(player.pos_x, player.pos_y -1)
        player.move(0, -1)
        score -= 1
    elif command == "a" and player.can_move(-1, 0, g):  # move left
        #maybe_item = g.get(player.pos_x -1, player.pos_y)
        player.move(-1, 0)
        score -= 1
    elif command == "i": # Check for inventory
        if inventory:
            print("Inventory:", ", ".join(inventory))
        else:
            print("You have nothing in your pack.")

    maybe_item = g.get(player.pos_x, player.pos_y)  # Varje ny player position checkas för föremål

    if isinstance(maybe_item, pickups.Item): # we found something
        score += maybe_item.value # Beroende på hittat föremål ökas Score
        inventory.append(maybe_item.name)  # funnet föremål läggs i inventory-listan
        print(f"You found a {maybe_item.name}, worth {maybe_item.value} points.")
        #g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
