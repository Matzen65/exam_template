from .grid import Grid
from .pickups import exit_list
from .player import Player
from . import pickups

player = Player(17, 5)
score = 0
inventory = []
moves = 0
show = 1

g = Grid()
g.set_player(player)
g.make_walls()
g.make_block_walls()
g.make_trap()
g.make_spade()
g.make_key()
g.make_treasure()
g.make_exit()
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q"]: #["q", "x"]:

    print("Number of moves", moves)
    mod = moves % 25
    #print("resten är just nu ", mod)
    #Här lägger vi ut en extra frukt efter 25 steg
    if mod == 0 and moves != 0:
        extra = pickups.randomize_extra(g)
        print(f"You are moving fast, one {extra}, Bonus fruit is placed on the game field!")
    moves += 1


    print_status(g)
    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1, 0, g, inventory):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        player.move(1, 0)
        score -= 1 # golvet är lava man förlorar ett poäng per steg
    elif command == "s" and player.can_move(0, 1, g, inventory):  # move down
        player.move(0, 1)
        score -= 1
    elif command == "w" and player.can_move(0, -1, g, inventory):  # move up
        player.move(0, -1)
        score -= 1
    elif command == "a" and player.can_move(-1, 0, g, inventory):  # move left
        player.move(-1, 0)
        score -= 1

    elif command == "i": # Check for inventory
        if inventory:
            print("Inventory's:", ", ".join(inventory))
        else:
            print("You have nothing in your pack.")

    maybe_item = g.get(player.pos_x, player.pos_y)  # Varje ny player position checkas för föremål

    if isinstance(maybe_item, pickups.Item):    # we found something
        score += maybe_item.value               # Beroende på hittat föremål ökas/minskas Score
        inventory.append(maybe_item.name)       # funnet föremål läggs i inventory-listan
        #print(maybe_item)
        ex_fruit = str(maybe_item)
        if ex_fruit in exit_list:
            exit_list.remove(ex_fruit)
            #print(exit_list)
        print(f"You found a {maybe_item.name}, worth {maybe_item.value} points.")
        #g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)

    #if maybe_item == "X":

    if maybe_item == ",":
        print("Ooouch!!! You fell in a trap, it cost you 10 points")
        # trap hamnar inte i Inventory
        score += -10

    if maybe_item == "#":
        print("You found a spade, put it in your inventory and use to remove a wall block!")
        inventory.append("spade")
        exit_list.remove("#")
        g.clear(player.pos_x, player.pos_y) # tar bort objektet från spelplanen

    if maybe_item == "P":
        print("You found a mystic Key, put it in your inventory, it might become useful!")
        inventory.append("key")
        exit_list.remove("P")
        g.clear(player.pos_x, player.pos_y) # tar bort objektet från spelplanen

    if maybe_item == "¤":
        if "key" in inventory:
            print("You use the key and find a treasure worth 100 points")
            print("Your key got stuck in the lock and removed from your pack")
            inventory.remove("key")
            exit_list.remove("¤")
            #print(exit_list)
            score += 100
            g.clear(player.pos_x, player.pos_y) # tar bort objektet från spelplanen

    #print("du har", len(exit_list), "föremål kvar att finna")

    if len(exit_list) == 3:
        if show == 1:
            print("Good job, almost done! Out of nowhere an Exit door appeared.")
            print("The door will unlock after you found those 3 missing elements,")
            g.make_exit()
            show = 0
        print(" Missing elements ",exit_list)


    if maybe_item == "E":
        if len(exit_list) == 0:
            #if len(exit_list) == 8:
            print("Congratulations, you have won the game!")
            command = "q"  # command "x" är avaktiverat
        else: print(f" Sorry the door is not yet active, you need to find those item to unlock, {exit_list}")

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")