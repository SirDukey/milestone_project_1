SERVER = 'localhost'
PORT = 27017
DATABASE = 'project1'

CONFIGS = {
    "selection": {
        "type": "selection",
        "a": "select_add",
        "u": "select_update",
        "r": "select_remove",
        "l": "select_list",
        "s": "select_search"
    },
    "prompt": {
        "type": "prompt",
        "prompt": "\nwelcome to the movies database\na - to add a movie\nu - to update a movie\nr - to remove a "
                  "movie\nl - to list movies\ns - to search for a movie\nq - to quit\nchoose from the options: "
    },
    "sorting": {
        "type": "sorting",
        't': 'title',
        'y': 'year',
        'd': 'director'

    }
}
