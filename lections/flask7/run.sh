echo Run db upgrade
flask db migrate
echo Run application
flask run -h 0.0.0.0 -p 5000
