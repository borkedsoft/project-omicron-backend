Getting started
===============

Commands to set up an instance of the backend:

    git clone "https://github.com/borkedsoft/project-omicron-backend.git"
    cd project-omicron-backend
    python -m venv .
    . bin/activate
    pip install -r requirements.txt
    cd omicron
    # for development, don't set DJANGO_DEBUG for deployment
    export DJANGO_DEBUG=True
    export DJANGO_SECRET_KEY="very secret key"
    ./manage.py migrate
    ./manage.py runserver

You can put static files in omicron/static for development,
just `cp -r omicron-frontend/build/* static`. (also you need to remove the hashes from the built output, TODO: change webpack config to not need that)
