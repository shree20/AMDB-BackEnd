class Movie:
    """A sample Employee class"""

    def __init__(self, name, director):
        self.name = name
        self.director = director

    def __repr__(self):
        return "Movie('{}', '{}', {})".format(self.title, self.director)