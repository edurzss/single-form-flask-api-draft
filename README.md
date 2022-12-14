# Flask API Draft

A simple flask API draft with a single form in the frontend.
Used for a credit risk analysis project where the goal is to predict whether a person will be able to pay off their debt, based on data provided through the form.

Composed by three microservices:
* API
* Redis
* ML Service

## How to build and run
    docker compose up --build

Run docker compose command to test it.

## About the form
The form was crafted to load data similar to the provided by the [PAKDD2010 Dataset](https://www.kaggle.com/competitions/pakdd2010-dataset/overview).
Prediction for this draft is hardcoded, so you need to load your model at ml_service.py