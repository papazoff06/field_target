web: python manage.py migrate && python manage.py createsuperuser --noinput || true && gunicorn field_target.wsgi:application --bind 0.0.0.0:$PORT

