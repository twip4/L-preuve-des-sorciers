class Sorcier:
    def __init__(self, mana):
        self.mana = mana
        self.position = (0, 0)

    def move(self, direction):
        if direction == "DOWN":
            self.position = self.position[0] - 1, self.position[1]
        elif direction == "RIGHT":
            self.position = self.position[0], self.position[1] + 1
        else:
            print("error")

    def set_mana(self, mana):
        self.mana += mana
        return self.mana

    def get_position(self):
        return self.position

    def affiche(self):
        print("nb mana : " + str(self.mana))
        print("position : " + str(self.position))
