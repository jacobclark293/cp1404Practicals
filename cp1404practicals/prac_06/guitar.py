class Guitar:
    """Represent information about a guitar"""

    def __init__(self, name, year, cost):
        """Construct a guitar from the given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Determine how old a guitar is"""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage or not"""
        return self.get_age() >= 50
