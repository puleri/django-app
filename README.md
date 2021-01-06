
# Zone Back-End (Django)

## Summary

If forking and cloning this, be sure to use a python shell with
`pipenv shell` and then run your local server with `python manage.py runserver`

The backend was created with python and the Django framework.

### My Development Process

1. Lay out estimated schedule.
1. Begin by reviewing documentation and working django back-ends for reference.
1. Build Project models.
1. Create Project routes.
1. Create/Test curl-scripts for project CRUD.
1. Create serializers
1. Run makemigragtions/migrate in terminal
1. Debug by conferring with peers.
1. Deploy


## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## Future iterations

In future iterations of the app I would like to utilise bootstrap in project forms,
allow for more interaction and more information to be displayed on the index of
projects.


