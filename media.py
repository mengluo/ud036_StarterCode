class Movie():
    """This class defines various properties and a behavior of a movie"""
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube):
        """This is the constructor for Movie class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
