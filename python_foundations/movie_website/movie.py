import webbrowser


class Movie():
    """Movie: way to store movie data and interact with this data"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
