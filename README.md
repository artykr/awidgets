# AWidgets API

## Installation and setup

### Setup with Poetry

This project uses Poetry to manage dependencies.
Please find `poetry` installation instructions here: https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions.

Run the following command-line scripts:

1. `prestart-poetry.sh`. This will install the dependencies, create and pre-populate the database.
NOTE: if you're using `pyenv` make sure to uncomment appropriate line in `prestart-poetry.sh`
to disable virtual environments creation in `poetry`.
2. `start.sh`. This will spin up a local web-server at port `8000`.

### Setup with pip

If you prefer not to use poetry `requirements.txt` file is available as a fallback. It also includes
development dependencies.

Run the following command-line scripts:

1. `prestart-poetry.sh`. This will install the dependencies, create and pre-populate the database.
2. `start.sh`. This will spin up a local web-server at port `8000`.

### Environment

You can set the following environment variables to change the application settings:

- `PROJECT_NAME`: name of the application. Default value: `Awidgets`.
- `DB_NAME`: name of SQLite database without `.db` extension. Default value: `awidgets`.
- `DEFAULT_LIST_RESPONSE_LIMIT`: default maximum number of items to return from a query
to get a list of widgets. Default value: `100`.

## Checks and tests

You can run the following commands in the project folder to run various check and tests:

- `pylint awidgets`: runs a linter.
- `mypy awidgets`: runs typechecking.
- `black awidgets`: re-formats the code.
- `bandit -r awidgets`: runs security scan.
- `pytest`: runs tests.

## Usage

You can access the API at http://localhost:8000 by default. OpenAPI documentation is available at
http://localhost:8000/docs.

## Example Requests

### Get a list of widgets

The list is limited to 3 widgets starting at the second one. Widgets are sorted by `id`.
`X-Total-Count` response header includes a total number of widgets in the database. 

```shell
curl -X GET --location "http://localhost:8000/widgets/?limit=3&skip=1" \
    -H "Accept: application/json"
```

### Get a single widget

```shell
curl -X GET --location "http://localhost:8000/widgets/2" \
    -H "Accept: application/json"
```

### Create a new widget

```shell
curl -X POST --location "http://localhost:8000/widgets/" \
    -H "Content-Type: application/json" \
    -d "{
          \"name\": \"My Awesome Widget\",
          \"number_of_parts\": 3
        }"
```

### Update an existing widget

```shell
curl -X PUT --location "http://localhost:8000/widgets/1" \
    -H "Content-Type: application/json" \
    -d "{
          \"name\": \"My Super-Awesome Widget\",
          \"number_of_parts\": 2
        }"
```

### Delete a widget

```shell
curl -X DELETE --location "http://localhost:8000/widgets/3"
```

## Future improvements for a larger-scale application

- Authentication/Authorization.
- Settings management using Pydantic.
- Use DateTime fields with proper timezone handling.
- Add additional parameters for the list widgets endpoint (sorting, filtering).
- Add `Link` headers for pagination.
- Add API versioning.
- Add partial updates with PATCH.