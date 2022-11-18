# Python classes practice

## Homework
- Create models, views and forms for Plants
- Create simple templates (for example you have auth logic)

## Local setup

**Create python environment**

```
$ python3 -m venv .venv
```

**Activate python environment**

```
$ source .venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Run database container**

```
$ docker-compose up -d db
```

**Add migrations to database**

```
$ flask db migrate
```

**Run application**

```
$ flask run
```

## Setup with docker

```
$ docker-compose up -d --build
```
