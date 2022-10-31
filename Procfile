release: sh -c 'python manage.py migrate && python manage.py loaddata initial_testimoni.json'
web: gunicorn lelang_donasi.wsgi --log-file -