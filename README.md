# brick-query-ui

This repository contains a [Flask]() application used to perform interactive queries on a [Brick]() ontology semantic model. The
objective is to provide a quick and easy way to write validate and perform queries.

![mortar-paper](./static/img/app.png "Example of timeseries from query on timescald db and brick model")

## Setup

First of all install equired pachages from the requirement files.

```bash
pip install -r requirements.txt
```

## Local deployment

Run flask application with the following command

```bash
flask run
```

You should see something like this

```bash
* Environment: production
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now visit the `http://127.0.0.1:5000/` url to access the flask application.

## Docker deployment

The script folder contains some shell scripts useful to deploy the flask application using Docker. Execute
the `start.sh` script to create the Docker image and build a container from the resulting image:

```bash
bash scripts/start.sh
```

Once the script finishes running, use the following command to list all running containers:

```bash
docker ps
```

```bash
bash scripts/cleanup.sh
```

## Built with
CodeMirror
Brick
Bootstrap
Flask

## Cite

## License