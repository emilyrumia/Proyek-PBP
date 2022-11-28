release: sh -c 'python manage.py migrate && python manage.py loaddata initial_testimoni.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_faq.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_pertanyaan.json'
web: python manage.py migrate && gunicorn lelang_donasi.wsgi
