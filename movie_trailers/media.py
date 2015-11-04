''' Class for movie info.

    GNU General Public Licence.

'''

###Created by Ramiro Trejo, 2015. 

import webbrowser

class Movie():
    ''' This class provides a way to store movie related information

    Attributes:
        title: A string indicating title of movie.
        trailer_youtube_url: A url string of trailer from movie.
        poster_image_url: A url string to movie poster.
        date_released: A string containing year of movie release. ex. "2015".
        director: A string of the name of director.
        genre: A string of the movie genre.
        duration: A string of the lenght of movie.

        '''


     #constructor of Movie class
    def __init__(self, movie_title, trailer_youtube, poster_image, date_released, director, genre, time_duration):
        ''' Inits Movie object with movie data.

        '''
         self.title = movie_title
         self.trailer_youtube_url = trailer_youtube
         self.poster_image_url = poster_image
         self.date_released = date_released
         self.director = director
         self.genre = genre_list
         self.duration = time_duration

     #opens trailer in the browser
    def show_trailer(self):
        ''' Opens the movie trailer in browser.

        Args:
            self.

        Returns:
            Opens url of the movie object in a browser.

        Raises:
            None.

        '''
         webbrowser.open(self.trailer_youtube_url)
