#!/usr/bin/env sh

echo Run django migrations
python manage.py migrate || exit 0
echo Collect staticfiles
python manage.py collectstatic --noinput --clear || exit 0

chmod -R 755 staticfiles/

exec "$@"
