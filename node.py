class Room:

    pres_wall = 0
    pres_hole = 0
    pres_monster = 0
    pres_gold = 0
    pres_smell = 0
    pres_wind = 0

    pres_teleport = 0

    conn_remained = 0
    conn_exist = 0

    isChanged = False

    numOfMonstersToLeave = 0
    numOfMonstersToReturn = 0


    neighbors = []
    isNormal = True


    def __init__(self, id):
        self.id = id
        self.monsters = []

    def toString(self):
        if self.isNormal == True:
            return "Room {}, Normal, Monster: {}, Hole: {}, Wall {}, Gold {}, Teleport: {}, Wind {}, Smell {} \n".format(self.id, self.pres_monster, self.pres_hole, self.pres_wall, self.pres_gold,
                    self.pres_teleport, self.pres_wind, self.pres_smell)
        else:
            return "Room {}, Border, Monster: {}, Hole: {}, Wall: {}, Gold: {}, Teleport: {}, Wind: {}, Smell: {} \n".format(self.id,
                    self.pres_monster, self.pres_hole, self.pres_wall, self.pres_gold,  self.pres_teleport, self.pres_wind, self.pres_smell)