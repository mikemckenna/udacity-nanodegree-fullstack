import movie
import fresh_tomatoes
import webbrowser  # timer

strange_brew = movie.Movie("Strang Brew",
                           "Two brothers take on an evil brewmeister",
                           "https://upload.wikimedia.org/wikipedia/en/6/6e/Strange_Brew_%28theatrical_poster%29.jpg",
                           "https://www.youtube.com/watch?v=oMI23JJUpGE",)


gleaming_cube = movie.Movie("Gleaming the Cube",
                            "A 16-year-old skateboarder investigates the death of his adopted Vietnamese brother.",
                            "https://upload.wikimedia.org/wikipedia/en/5/5e/Gleaming_the_cube.jpg",
                            "https://www.youtube.com/watch?v=yviIgIDxlwc")

karate_kid = movie.Movie("Karate Kid",
                         "He taught him the secret to karate is in mind & heart...not in the hands",
                         "https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg",
                         "https://www.youtube.com/watch?v=yDi3an8WgN4")

goonies = movie.Movie("The Goonies",
                      "Facing foreclosure of their homes, a group of children gather for a last weekend.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg",
                      "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

space_camp = movie.Movie("Space Camp",
                         "Four teenagers go to space camp at Kennedy Space Center to learn about the NASA space program.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b2/Space_camp_-_1986_Poster.png",
                         "https://www.youtube.com/watch?v=0Umy8VTiKG4")

war_games = movie.Movie("War Games",
                        "Would you like to play a game?",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg",
                        "https://www.youtube.com/watch?v=xogbyv108kI")

movies = [strange_brew, gleaming_cube, karate_kid,
          goonies, space_camp, war_games]

fresh_tomatoes.open_movies_page(movies)

print (movie.Movie.VALID_RATINGS)
print (movie.Movie.__doc__)
print (movie.Movie.__name__)
print (movie.Movie.__module__)
