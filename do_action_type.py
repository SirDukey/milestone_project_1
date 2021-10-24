from action_types import *
from db import get_config


def select_add():
    title = input('title: ')
    year = input('year: ')
    director = input('director: ')
    if title == '' and year == '' and director == '':
        print('nothing to add')
        return
    added = add_movie({
        'title': title,
        'year': year,
        'director': director
    })
    if added.acknowledged:
        print('added {} to the database'.format(title))


def select_update():
    title = input('title: ')
    movie = search_movies(title)
    year = input('year: ({}) '.format(movie.get('year')))
    if year == '':
        year = movie.get('year')
    director = input('director: ({}) '.format(movie.get('director')))
    if director == '':
        director = movie.get('director')
    updated = update_movie({
        'title': title,
        'year': year,
        'director': director
    })
    if updated.acknowledged:
        print('updated {}'.format(title))


def select_remove():
    title = input('title: ')
    removed = remove_movie({
        'title': title
    })
    if removed.acknowledged:
        print('removed {}'.format(title))


def select_list():
    sorting = input('sort by (t)itle, (y)ear or (d)irector: ')
    sorted_movie_list = list_movies(sorting)
    if not sorted_movie_list:
        return
    for movie in sorted_movie_list:
        print('{} ({}), directed by {}'.format(
            movie.get('title'), movie.get('year'), movie.get('director')
        ))


def select_search():
    pattern = input('search in title: ')
    movies_found = search_movies(pattern)
    if movies_found:
        print('found the following movies:')
        for movie in movies_found:
            print('{} ({}), directed by {}'.format(
                movie.get('title'),
                movie.get('year'),
                movie.get('director')
            ))
    else:
        print('no movie found with {} in the title'.format(pattern))


def perform_selection(selection):
    selections = get_config('selection')
    if selection in selections.keys():
        select_function = eval(selections[selection])
        select_function()
    else:
        print('unknown option, try again!\n')
