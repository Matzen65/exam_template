
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

    def can_move(self, dx, dy, grid): # kollar 1 steg framåt i rörelseriktningen
        new_pos_x = self.pos_x + dx
        new_pos_y = self.pos_y + dy

        if grid.get(new_pos_x, new_pos_y) == grid.wall:
            print("You can't exit from the game field !!!")
            return False # Returnera False om det står något i vägen

        if grid.get(new_pos_x, new_pos_y) == grid.block_wall:
            print("You need to blow this wall to pass !!!")
            return False # Returnera False om det står något i vägen

        return True
        #TODO: returnera True om det inte står något i vägen


