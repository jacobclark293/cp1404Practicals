from musician import Musician
# from guitar import Guitar


class Band():

    def __init__(self, name):
        """Initialise a band"""
        self.name = name
        self.members = []

    def __str__(self):
        # return f"{self.name} ({self.members})"
        return f"{super().__str__()} plus test"

    def __repr__(self):
        return str(vars(self))

    def add(self, member):
        """"""
        self.members.append(member)

    def play(self):
        for member in self.members:
            return f"{self.members[0]} is playing: something"
