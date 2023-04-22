# recipe-app-api
Recipe API Project.


#  docker commands

- run django app: `docker-compose run --rm app sh -c "python manage.py runserver"` or `docker-compose up` because it's defined in there as well
- `docker-compose run --rm app sh -c "python manage.py test"`to run python tests in docker container