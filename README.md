People
======

http://ef-founder-school-people.herokuapp.com/

http://effounderschool.com

Local Development
-----------------

### Requirements

- [Heroku Toolbelt](https://toolbelt.heroku.com/)
- [heroku-config](https://devcenter.heroku.com/articles/config-vars#using-foreman-and-heroku-config)
- [Postgres.app](http://postgresapp.com/)

### Installation

1.

```sh
git clone git@github.com:joinEF/people.git
cd people

# Create and enter virtual environment.
virtualenv venv
source venv/bin/activate

# Install Python dependancies.
pip install -r requirements.txt

# Link up to Heroku app.
heroku git:remote --app ef-founder-school-people

# Set up local configuration.
# Set local development specific variables and then
# fill in the rest from remote Heroku config.
echo DATABASE_URL=postgres://$USER@localhost/people > .env
echo DJANGO_DEBUG=true >> .env
echo PORT=8000 >> .env
heroku config:pull
for variable in `cat .env`; do; export $variable; done;
unset SEGMENT_IO_API_WRITE_KEY
```

2. Either 2. a. or 2. b.

2. a. Pull database from remote to local.

```sh
createdb people
heroku pg:pull DATABASE_URL people
```

2. b. Create database from scratch.

```sh
createdb people
python manage.py syncdb --noinput
python manage.py migrate
python manage.py createsuperuser
```

### Running web server

```sh
python manage.py runserver 0.0.0.0:$PORT
```

### Accessing site

```sh
open http://127.0.0.1:$PORT
```

Deployment
----------

```sh
heroku config:remove DJANGO_DEBUG
heroku config:set DJANGO_SECRET_KEY=
git push heroku master
```

Resources
---------

Django on Heroku
https://devcenter.heroku.com/articles/getting-started-with-django

Heroku Config
https://devcenter.heroku.com/articles/config-vars

Getting started as a collaborator
https://devcenter.heroku.com/articles/collab