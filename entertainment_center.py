'''List of movies rendered in a HTML page and opened in a browser. '''
# Created by Ramiro Trejo, 2015.

import media
import fresh_tomatoes


# creating instances of class Movie
goonies = media.Movie(
                "Goonies",
                "https://www.youtube.com/watch?v=kFEfHCJG4G4",
                "https://upload.wikimedia.org/wikipedia/" +
                "en/c/c6/The_Goonies.jpg",
                "1985",
                "Richard Donner",
                "Adventure",
                "114")

blade_runner = media.Movie(
                "Blade Runner",
                "https://www.youtube.com/watch?v=hiH4hxhKBmY",
                "https://upload.wikimedia.org/wikipedia/" +
                "en/5/53/Blade_Runner_poster.jpg",
                "1982",
                "Ridley Scott",
                "Science Fiction",
                "116")

juno = media.Movie(
                "Juno",
                "https://www.youtube.com/watch?v=K0SKf0K3bxg",
                "https://upload.wikimedia.org/wikipedia/en" +
                "/e/ec/Junoposter2007.jpg",
                "2007",
                "Jason Reitman",
                "Drama",
                "96")

inception = media.Movie(
                "Inception",
                "https://www.youtube.com/watch?v=1g4PLj0PlOM",
                "https://upload.wikimedia.org/wikipedia/en" +
                "/7/7f/Inception_ver3.jpg",
                "2010",
                "Christopher Nolan",
                "Thriller",
                "148")

pans_labyrinth = media.Movie(
                "Pan's Labyrinth",
                "https://www.youtube.com/watch?v=EqYiSlkvRuw",
                "https://upload.wikimedia.org/wikipedia/en" +
                "/6/67/Pan%27s_Labyrinth.jpg",
                "2006",
                "Guillermo del Torro",
                "Fantasy",
                "119")

space_oydessy_2001 = media.Movie(
                "2001: A Space Odyssey",
                "https://www.youtube.com/watch?v=E8TABIFAN4o",
                "https://upload.wikimedia.org/wikipedia/en" +
                "/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                "1968",
                "Stanley Kubrick",
                "Science Fiction",
                "142")

terminator_2 = media.Movie(
                "Terminator 2: Judgement Day",
                "https://www.youtube.com/watch?v=F1os6UU6jhU",
                "https://upload.wikimedia.org/" +
                "wikipedia/en/8/85/Terminator2poster.jpg",
                "1991",
                "James Cameron",
                "Science Fiction",
                "136")

elm_street = media.Movie(
                "A Nightmare on Elm Street",
                "https://www.youtube.com/watch?v=dCVh4lBfW-c",
                "https://upload.wikimedia.org/wikipedia/en" +
                "/a/a1/Nightmare01.jpg",
                "1984",
                "Wes Craven",
                "Horror",
                "91")

# holds all movie objects in a list
list_fav_movies = [
            goonies,
            blade_runner,
            juno,
            inception,
            pans_labyrinth,
            space_oydessy_2001,
            terminator_2,
            elm_street]

# opens html page with movie data embedded
fresh_tomatoes.open_movies_page(list_fav_movies)
