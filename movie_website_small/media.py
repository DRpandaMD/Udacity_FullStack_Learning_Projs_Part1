import webbrowser

class Movie(object):
    """This is a class for movies.  It contains the movie title, a storyline, 
    the poster url and a video trailer url"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        return

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        return

