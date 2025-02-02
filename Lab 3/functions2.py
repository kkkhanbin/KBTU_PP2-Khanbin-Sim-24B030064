# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def is_good(name: str) -> bool:
    for movie in movies:
        if movie["name"] == name and movie["imdb"] > 5.5:
            return True
    return False


def good_movies() -> list:
    good_movies = []

    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie)
    
    return good_movies


def movies_by_category(category: str) -> list:
    new_movies = []

    for movie in movies:
        if movie["category"] == category:
            new_movies.append(movie)
    
    return movies


def avg_imdb_by_category(category: str) -> float:
    new_movies = movies_by_category(category)
    if len(new_movies) == 0:
        return 0
    return sum(map(lambda x: x["imdb"], new_movies)) / len(new_movies)


def main():
    print(good_movies())
    print(movies_by_category("Romance"))
    print(avg_imdb_by_category("Detective"))


if __name__ == "__main__":
    main()