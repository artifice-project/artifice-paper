# Artifice Paper
[![Build Status](https://travis-ci.org/minelminel/flask-boilerplate.svg?branch=master)](https://travis-ci.org/minelminel/flask-boilerplate)

## Installation

First, clone the repository and create a virtualenv. Then install the requirements:

`$ pip install -e .`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```sql
CREATE DATABASE flask_paper;
CREATE DATABASE flask_paper_test;
```

Now you can create the tables using Alembic:
```bash
artifice.paper db upgrade
```

Finally you can run the application:
```bash
artifice.paper runserver
```

or play in the Python REPL:
```bash
artifice.paper shell
```

In order to run unit tests in py.test invoke:
```bash
artifice.paper test
```

To view test coverage:
```bash
artifice.paper coverage
```

There is a preconfigured WSGI module located at `artifice.paper.core.wsgi`. Example usage with Gunicorn:
```bash
gunicorn --workers 1 --bind 0.0.0.0:8000 artifice.paper.core.wsgi:application
```

If the process fails to start, try prepending the `gunicorn` with its relative path within your virtual environment, for example `env/bin/gunicorn ...`
