release: sh -c 'python manage.py migrate && python manage.py loaddata initial_testimoni.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_faq.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_pertanyaan.json'
web: gunicorn lelang_donasi.wsgi --log-file -
