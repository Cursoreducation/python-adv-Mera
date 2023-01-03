# Use an official Python runtime based on Debian 10 as a parent image.
FROM python:3.11-alpine

# Set work directory
WORKDIR /usr/src/app

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1
# 2. Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# 3. Install fault handlers for the SIGSEGV, SIGFPE, SIGABRT, SIGBUS, and SIGILL signals
ENV PYTHONFAULTHANDLER 1
# 4. Disable pip's cache files in the container
ENV PIP_NO_CACHE_DIR off
# 5. Don’t periodically check PyPI to determine whether a new version of pip is available for download
ENV PIP_DISABLE_PIP_VERSION_CHECK on
# 6. Keeps Poetry from automatically creates virtual environments
ENV POETRY_VIRTUALENVS_CREATE false

RUN \
  apk add --no-cache curl

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# Install the project requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code of the project into the container.
COPY . .

# start gunicorn, using a wrapper script to allow us to easily add more commands to container startup:
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
RUN chmod a+x /usr/src/app/docker-entrypoint.sh

# Runtime command that executes when "docker compose run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
CMD set -xe; gunicorn --bind 0.0.0.0:8000 config.wsgi:application --workers 2
