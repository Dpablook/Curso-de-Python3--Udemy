class player:

    def __init__(self, **kwargs):
        self.hit = kwargs.get("hit",50)
        self.mana = kwargs.get("mana",50)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo","Puff")

