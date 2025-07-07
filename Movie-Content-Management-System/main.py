from Filter.GenreFilter import GenreFilter
from Filter.RatingFilter import RatingFilter
from Filter.SingleSearch import SingleSearch
from Filter.YearFilter import YearFilter
from Service.SearchService import SearchService

while True:
    command = input("Enter Command")

    if command == 'ADD_USER':
        from Model.User import User
        user_obj = User(1, 'Mohammad Talha', 'Action')
        user_obj.user_service.create_user(user_obj)

    if command == "ADD_MOVIE":
        from Model.Movie import Movie
        movie_obj = Movie(1, 'Inception', 'Action', 2018, 9.1)
        movie_obj.movie_service.create_movie(movie=movie_obj)

    if command == 'SEARCH':
        search_type = input("Enter Search type")
        search = None
        filter_list = []
        if search_type == 'GENRE':
            enter_genre = input("Enter Genre type")
            genre_filter = GenreFilter(enter_genre)
            filter_list.append(genre_filter)

        if search_type == 'year':
            enter_year = input("Enter year")
            year_filter = YearFilter(enter_year)
            filter_list.append(year_filter)

        if search_type == 'rating':
            enter_rating = input("Enter rating")
            rating_filter = RatingFilter(enter_rating)
            filter_list.append(rating_filter)

        single_search = SingleSearch(filter_list)
        search = SearchService.search(1,single_search)
