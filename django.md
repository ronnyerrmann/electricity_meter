## Django

following [https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment]

Commands for Project and App:
```commandline
django-admin startproject meter_django
cd meter_django/
python3 manage.py startapp electricity
```
(compared to the example: `locallibrary` -> `meter_django` and `catalog` -> `electricity`)

Saved the `SECRET_KEY` in a file `meter_django/meter_django/secret.py`