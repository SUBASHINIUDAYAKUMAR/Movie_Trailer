import fresh_tomatoes
import media
#Creating instance for Alaipayuthey
Alaipayuthey=media.Movie("Alaipayuthey", 
                        "The story is based on a love story",
                        "https://lh3.googleusercontent.com/T8q1yAG5FlDjhzYDQI-tOP9DBjn424hrFwlb1OQ7dENRz3atOoqPJircqgcRY3JNbGIhABTMSw=w300",
                        "https://www.youtube.com/watch?v=BRFdGc3ku-k")
#Creating instance for Ayudhaezhuthu
Ayudhaezhuthu=media.Movie("Ayudha ezhuthu",
                 "The story sequel of politics and love",
                 "https://www.filmibeat.com/img/2017/01/ayuthaezhuthumollywoodretake-03-1483445850.jpg",
                 "https://www.youtube.com/watch?v=kiuOvdYBCzI")
#Creating instance for Aasai
Aasai=media.Movie("Aasai",
                  "Aasai, the movie is about two young lovers",
                  "https://www.filmibeat.com/img/220x80x275/popcorn/movie_posters/aasai-6288.jpg",
                  "https://www.youtube.com/watch?v=PlSZT05ayUA")
#Creating instance SillunuOruKaadhal
SillunuOruKaadhal=media.Movie("Sillunu Oru Kaadhal",
                     "A happily married man faces an emotional conflict, when his past lover comes back into his life.",
                     "https://s-media-cache-ak0.pinimg.com/originals/bc/37/1c/bc371c085b0c952367a33a7309696d8e.jpg",
                     "https://www.youtube.com/watch?v=tJ6wFu7DIc8")
#Creating instance for Ghilli
Ghilli=media.Movie("Ghilli",
                     "Velu, an aspiring kabaddi player, a powerful man keen on marrying the girl against her wish.",
                     "http://sim04.in.com/c99e45c6a0043b031f3544304b3472dc_m.jpg",
                     "https://www.youtube.com/watch?v=dS02g4mUvws")
#Creating instance for RajaRani
RajaRani=media.Movie("RajaRani",
                    "Newly weds who hate each other come to terms with each other and their past.",
                    "https://lh3.googleusercontent.com/-_oxCCoyvDT7CjQW2aprNygXgfiSrnyX7AS4I7ridfhgKRo3CRO4itOjtAKKLW6oT8aJ",
                    "https://www.youtube.com/watch?v=q6hMWYND4jQ")
#Putting those objects in a list
movies=[Alaipayuthey,Ayudhaezhuthu,Aasai,Ghilli,RajaRani]
#Calling open_movies_page() function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
