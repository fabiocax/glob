#!/bin/bash
cd /code
uwsgi --ini blog.ini
#./manage.py runserver 0.0.0.0:7000 --insecure
