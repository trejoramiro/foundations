import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    #global variable
    #VALID_RATINGS = ["G","PG","PG-13","R"]


     #constructor of Movie class
    def __init__(self, movie_title, movie_storyline, trailer_youtube, poster_image, date_released, director, genre_list, time_duration):
         self.title = movie_title
         self.storyline = movie_storyline
         self.trailer_youtube_url = trailer_youtube
         self.poster_image_url = poster_image
         self.date_released = date_released
         self.director = director
         self.genre = genre_list
         self.duration = time_duration

     #opens trailer in the browser
    def show_trailer(self):
         webbrowser.open(self.trailer_youtube_url)
