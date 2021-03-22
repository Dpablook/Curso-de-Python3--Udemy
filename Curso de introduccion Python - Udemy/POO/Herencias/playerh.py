class Player(object):
    vocation = "No vocation"
    spell="Puff"
    movement= "50"

    def __init__(self, **kwargs):
        self.hit = kwargs.get("hit",50)
        self.mana = kwargs.get("mana",50)

    def cast_spell(self):
        return self.spell


class paladin(Player):
    vocation = "Paladin"
    spell = "Pluff"
    movement = "200"

class archimaga(Player):
    vocation = "Archimaga"
    spell = "EXPLOSIOOON"
    movement = "2"