import fresh_tomatoes
import media

''' here creating the object of Movie class and
initialising the object with their name, movie's certification and genre,
url of movie poster and url of movie trailer'''


ironman1 = media.Movie(
                       "Ironman1",
                       "Certified: PG-13",
                       "Genre: fantacy/science fiction/action",
                       "https://bit.ly/2rLG8b8",
                       "https://www.youtube.com/watch?v=8hYlB38asDY"
                       )

ironman2 = media.Movie(
                       "Ironman2",
                       "Certified: PG-13",
                       "Genre: fantacy/science fiction/action",
                       "https://bit.ly/2rYgr4E",
                       "https://www.youtube.com/watch?v=BoohRoVA9WQ"
                       )

ironman3 = media.Movie(
                       "Ironman3",
                       "Certified: PG-13",
                       "Genre: fantacy/science fiction/action",
                       "https://bit.ly/2GU8X7F",
                       "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc"
                       )

the_avengers = media.Movie(
                           "The Avengers",
                           "Certified:  PG-13",
                           "Genre:  Fantasy/Science fiction",
                           "https://bit.ly/1N3f5G7",
                           "https://www.youtube.com/watch?v=1hPpG4s3-O4"
                           )

age_of_ultron = media.Movie(
                            "Avengers: Age of ultron",
                            "Certified: PG-13",
                            "Genre:  Fantasy/Science fiction",
                            "https://bit.ly/2IRk6vB",
                            "https://www.youtube.com/watch?v=tmeOjFno6Do"
                             )

infinity_war = media.Movie(
                           "Avengers: Infinity war",
                           "Certified:  PG-13",
                           "Genre:  Fantasy/Science fictionf5",
                           "https://bit.ly/2KjSEUq",
                           "https://www.youtube.com/watch?v=QwievZ1Tx-8"
                           )
# storing the object of the class movie in the format of list
movies = [ironman1, ironman2, ironman3,
          the_avengers, age_of_ultron, infinity_war]

# open the specified movie website page on the default browser
fresh_tomatoes.open_movies_page(movies)
