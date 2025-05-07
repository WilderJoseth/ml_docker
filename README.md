# Machine learning projects with docker

This repository storeds machine learning projects which have been deployed using docker containers.

## Adult income

This project uses a binary classification model to make predictions.

* It has two sub projects with its own container:
  * **ml_process**: to train models.
  * **web_app**: to run a web app that uses trained models.

Create volume.

```bash
docker volume create adult-income-vl
```

Create image and container for ml_process (input/data is required).

```bash
docker build -t adult-income-ml .
docker run --name ml_process -v adult-income-vl:/app/output adult-income-ml
```

Create image and container for web_app.

```bash
docker build -t adult-income-app .
docker run --name web_app -dp 127.0.0.1:5000:5000 -v adult-income-vl:/app/input adult-income-app
```
