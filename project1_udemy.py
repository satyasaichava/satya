movies = []
def print_movie(movie):
    print(f'title : {movie["title"]}')
    print(f'director : {movie["director"]}')
    print(f'year : {movie["year"]}')

def movie_add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
    'title': title,
    'director': director,
    'year': year
    })
def movie_list():
    if movies == []:
        print('no movies added yet')
    else:
        for movie in movies:
            print(f'title : {movie["title"]}')
            print(f'director : {movie["director"]}')
            print(f'year : {movie["year"]}')
def find_movie():
    if movies == []:
        print('no movies added yet')
    else:
        user_title = input('enter movie name')
        for movie in movies:
             title = movie['title']
             if title.lower() == user_title.lower():
                  print_movie(movie)
                  break
        else:
            print('the movie you are searching for is not available')
                

selection = input('please enter following alphabets for respective actions: \n a --> add a new movie \n f --> find a movie \n l --> list of movies \n q --> quit this carousel \n')

while selection != 'q':
    if selection == 'a':
        movie_add()
    elif selection == 'l':
        movie_list()
    elif selection == 'f':
        find_movie()
    else:
        print('Unknown command. Please try again.')
    selection = input('please enter following alphabets for respective actions: \n a --> add a new movie \n f --> find a movie \n l --> list of movies \n q --> quit this carousel \n')

print("you quit the carousel")
