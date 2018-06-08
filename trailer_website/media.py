import webbrowser


class Movie():
    """list of movie attributes:
    Attributes:
         movie_title(string):stores the name of movie
         movie_certification(string):it stores certification type of the movie
         movie_genre(string):it stores the genre of the movie
         poster_image(string):it stores the address of the iamge
         trailer_youtube(string):it stores the address of trailer of the movie
    """
    def __init__(self, movie_title, movie_certification, movie_genre,
                 poster_image, trailer_youtube):
        """
     self.title is storing the name of the movie
     self.certification is storing certification type of the movie
     self.genre is storing the genre of the movie
     self.poster_image_url is storing the url address of image
     self.trailer_youtube_url is storing the url address of trailer
    """

        self.title = movie_title
        self.certification = movie_certification
        self.genre = movie_genre
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# plays the trailer of the movie
    def show_trailer(self):
        # opens the web browser for playing youtube trailer
        webbrowser.open(self.trailer_youtube_url)
