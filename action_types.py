from db import movies, get_config


def add_movie(data):
    added = movies.insert_one(data)
    return added


def update_movie(data):
    title = data['title']
    updated = movies.update_one({
        'title': title
    }, {
        '$set': data
    })
    return updated


def list_movies(sorting):
    if sorting == '':
        sorting = 't'
    sorting_lookup = get_config('sorting')
    if sorting not in sorting_lookup.keys():
        print('not a valid sorting selection')
        return
    result = list(movies.find().sort(sorting_lookup[sorting], 1))
    if not result:
        print('database is empty')
    return result


def remove_movie(data):
    removed = movies.delete_one(data)
    return removed


def search_movies(pattern):
    result = list(movies.find({
        'title': {
            '$regex': pattern
        }
    }).sort('title', 1))
    return result
