class Monster:

    isBlocked = 0
    hasMoved = False
    willTeleport = False

    def __init__(self, id):
        self.id = id
       # self.isNormal = isNormal            # check if normal or border room

    def toString(self):
        return "Monster " + unicode(self.id)