import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story", 
                        "A story of his boys and his toys",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "Conflict of life interests on a foriegn planent",
                    "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                    "https://youtu.be/5PSNL1qE6VY")

the_matrix = media.Movie("The Matrix",
                        "You are the one Neo!",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
                        "https://youtu.be/vKQi3bBA1y8")

ip_man = media.Movie("Ip Man",
                    "A story of a Kung Fu master Ip Man",
                    "http://img.moviepostershop.com/ip-man-movie-poster-2008-1020698460.jpg",
                    "https://youtu.be/1AJxXQ7xojE")

the_lord_of_the_rings = media.Movie("The Lord of the Rings",
                                    "A story of brave Hobbit and his friends that fight to save MiddleEarth",
                                    "https://www.movieposter.com/posters/archive/main/105/MPW-52979",
                                    "https://youtu.be/V75dMMIW2B4")


princess_mononoke = media.Movie("Princess Mononoke",
                                "A story of a prince who fights a off demons to save his village.  Who later gets corrupted and seeks out a princess to find a cure to his corruption",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcS3ReuE3ksrdNabf0K7frhelHm-05ec4a_1mIxQUqNiRduHNrJ5",
                                "https://youtu.be/4OiMOHRDs14")

spirited_away = media.Movie("Sprited Away",
                            "A story of a young girl who finds her self and gains the courage to save her parents",
                            "https://celluloidwritings.files.wordpress.com/2015/07/spirited_away.jpg",
                            "https://youtu.be/ByXuk9QqQkk")

movies = [toy_story, avatar, the_matrix, ip_man, the_lord_of_the_rings, princess_mononoke, spirited_away]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
