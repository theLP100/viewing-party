
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    #create a dictionary with the keys 'title', 'genre', 'rating', and the values the values passed in
    if title and genre and rating:
        movie_dict = {}
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    #user_data is a dictionary with watched as one of the keys.
    #this function adds the movie_dict (listed here as movie) into a list stored as a value connected to watched.
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #this function will add a movie (which is a dict, remember) into the list stored as a value to the key 'watchlist' in the user_data dict.
    #user_data is a dictionary with 'watchlist' as one of the keys.
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    #This function takes in user_data (dict of watched and watched list 
    #find the movie in watchlist that has the movie_title.
    #iterate through the list, checking each dictionary. 
    
    movie_found = False

    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
            movie_found = True
            break

    if movie_found == True:
        #once you find this movie, we're going to take it off of watchlist and append it to watched.
        #print(user_data['watchlist'])
        #print(watched_movie)
        user_data['watchlist'].remove(watched_movie)
        user_data['watched'].append(watched_movie)

    return user_data

"""
#This ended up not working as expected.  Keeping it here in case I want it later.
def search(a_list, movie_title):
    #this helper function helps us search through a list and return the dictionary entry for the movie with the title of movie_hour
    #for elem in a_list:
        #if elem["title"] == movie_title:
            #return elem
        #else: 
            #return None
"""


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    #this takes in the user's data (a dictionary with 2 keys: watched and watchlist)
    #it outputs the average rating of all the movies in the dictionary 'watched'
    #I would like to save these values to a user...by making a class?  We'll see. 
    ratings_lst = []
    #this gives a list of ratings
    for movie in user_data["watched"]:
        ratings_lst.append(movie["rating"])


    #adding an if to deal with if it's an empty list:
    if len(ratings_lst) > 0:
        #this calculates the average:
        avg_rating = sum(ratings_lst) / len(ratings_lst)
        return avg_rating
    else: 
        return 0


def get_most_watched_genre(user_data):
    #This will make a dictionary, and add a count of how many times each genre appears. 
    genre_count = {}
    #keys will be genres (strings)
    #values will be the number of movies in that genre.
    #adding in an if to deal with if watched is an empty list:
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in genre_count:
                genre_count[genre] = 1
            else:
                genre_count[genre] += 1
        #now, genre_count is complete.  Let's return which key has the highest value associated with it.
        most_watched_genre = max(genre_count, key = genre_count.get)
        return most_watched_genre
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

