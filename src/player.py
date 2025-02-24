
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y


    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):

        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid,inventory): # kollar 1 steg framåt i rörelseriktningen
        #from src.game import inventory # Den här raden startar om spelet av någon anledning men behövs för spaden nedan
        new_pos_x = self.pos_x + dx
        new_pos_y = self.pos_y + dy

        #if grid.get(new_pos_x, new_pos_y) == grid.trap:
        #    print("Ooouch!!! You fell in a trap, it cost you 10 points")
            #score += -10

        if grid.get(new_pos_x, new_pos_y) == grid.wall:
            print("You can't exit from the game field !!!")
            return False # Returnera False om det står något i vägen

        if grid.get(new_pos_x, new_pos_y) == grid.block_wall:
            print("You need to dig this wall to pass !!!")

            if "spade" in inventory:
                print("You use your spade and dig through the wall")
                grid.set(new_pos_x, new_pos_y, ".")
                inventory.remove("spade")
                print("Your spade is wasted and you throw it away")
                #return True # Returnera True om spelaren har en spade att gräva genom muren med


            return False # Returnera False om det står något i vägen

        return True
        #TODO: returnera True om det inte står något i vägen

    def set(self, param, param1, empty):
        pass


