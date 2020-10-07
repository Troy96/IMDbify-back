# IMDbify-back
A Django REST Server that can be used to list movies (using scraping from IMDb), add a movie to watchlist, remove it and view the list, same for watchedlist.  The movies endpoint is used by IMDb-front to show movies on autocomplete.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ cd to/project/folder
$ pip install -r requirements.txt
```

Setup the Database
```bash
$ python manage.py migrate
```

Run the server
```bash
$ python manage.py runserver
```

The server should be running on http://127.0.0.1:8000
