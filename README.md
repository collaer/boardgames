# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Inspired from

This [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).
Related to this [repo](https://github.com/testdrivenio/django-on-docker).
Template boilerplate from [repo](https://github.com/Papagoat/django-bootstrap4-boilerplate).

The purpose is to build an hello world application to manage boardgames for Django discovery and exploratory exercise to determine best framework to use.

## Django version selection

Before proceeding let s consider the Django version.
Here I selected 3.1 which will be maintained until end of 2022.

3.2 next LTS will soon be available and should be migrated asap when done. ANother valid option should be using previous LTS 2.2 before switch to 3.2.

Consider [djangoproject Supported versions](https://www.djangoproject.com/download/) before starting.


## Model / db changes: Migrations

```sh
$ sudo docker-compose run web python manage.py makemigrations
$ sudo docker-compose run web python manage.py migrate
```

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:
    ```sh
    $ docker-compose up -d --build
    ```

    or

    ```sh
    $ sudo docker-compose up -d --build
    ```
1. create a superuser (admin user)
```sh
  sudo docker-compose run web python manage.py createsuperuser
```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.


    Also test the Django admin funcionalities http://localhost:8000/admin](http://localhost:8000/admin).

    App is published using the Django built in server capabilities. Not for production use, with the runserver option like this:

    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```

### Troubleshooting

Start with looking at the logs like this :

```sh
$ docker-compose logs -f
```

or

```sh
$ sudo docker-compose logs -f
```

To restart use
```sh
$ docker-compose down -v
```
before rebuilding (to drop db and rebuild it if passwords database names changes).


### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
    or

    ```sh
    $ sudo docker-compose -f docker-compose.prod.yml up -d --build
    ```    

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. **To apply changes, the image must be re-built**.

    App is published using nginx gunicorn webserver, may be used for production use.

    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```
