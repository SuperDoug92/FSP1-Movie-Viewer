# a library containing the movie object
import media
# a library which generates the html and css to display the movies on a page
import fresh_tomatoes

# creating movie objects
avatar = media.Movie("Avatar", "A movie about blue people",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

SOR = media.Movie("School of Rock", "A movie about school and rock and roll",
                  "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                  "http://www.youtube.com/watch?v=3PsUJFEBC74")

HG = media.Movie("Hunger Games", "A movie where hunger is a game",
                 "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                 "http://www.youtube.com/watch?v=PbA63a7H0bo")

# storing movie objects in array
movies = [avatar, SOR, HG]
# opening movies page in browser
fresh_tomatoes.open_movies_page(movies)
