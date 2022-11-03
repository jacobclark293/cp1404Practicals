class ProgrammingLanguage:
    """Represent information about a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic"""
        return self.typing == "Dynamic"
