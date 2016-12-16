import webbrowser
"""media.py contains a movie class

    The movie class stores data including the
    title, storyline, poster image url, and
    the trailer url.  It also contains a method
    called showTrailer which will open the
    trailer for the movie in a browser"""


class Movie():

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
