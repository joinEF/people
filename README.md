People
======

http://ef-founder-school-people.herokuapp.com/

http://effounderschool.com

Local Development
-----------------

```sh
export DATABASE_URL=postgres://$USER@localhost/people
export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY="development_django_secret_key"
python manage.py syncdb
python manage.py runserver 0.0.0.0:8000
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
