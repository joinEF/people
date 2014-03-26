People
======

http://founder-school-people.herokuapp.com/

Local Development
-----------------

```sh
export DATABASE_URL=postgres://$USER@localhost/people
export DJANGO_DEBUG=True
python manage.py syncdb
python manage.py runserver 0.0.0.0:8000
```

Resources
---------

Django on Heroku
https://devcenter.heroku.com/articles/getting-started-with-django