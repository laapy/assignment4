# Automated ML App Deployment with GitHub Actions and Docker

## Project Overview

This project is for Assignment 4 in Python for Machine Learning.

The purpose of this assignment is to build an automated CI/CD pipeline using GitHub Actions and Docker. Instead of focusing on training a complex machine learning model, this project focuses on deploying Python code automatically after it is pushed to a GitHub repository.

The pipeline runs tests and code quality checks, builds a Docker image, pushes the image to DockerHub, and deploys the container to a DigitalOcean server.

## Assignment Goal

The goal of this project is to complete the CD part of a CI/CD pipeline.

The workflow should behave as follows:

1. Code is committed and pushed to the `main` branch.
2. GitHub Actions automatically runs:
   - unit tests with `pytest`
   - type checking with `mypy`
   - linting with `pylint`
3. When the code is ready, changes are merged into the `prod` branch.
4. Pushing to the `prod` branch triggers the deployment workflow.
5. The deployment workflow:
   - runs the same checks as the `main` branch
   - builds a Docker image
   - pushes the Docker image to DockerHub
   - connects to the DigitalOcean server
   - pulls and runs the updated Docker container

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        ├── test.yml
        └── deploy.yml
