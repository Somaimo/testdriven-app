# Microservices with Docker, Flask, and React

Simple repo for the testdriven.io course.

## Running tests
You can run the unit tests, after starting the containers, with the following command:
```bash
docker-compose -f docker-compose-dev.yml run users python manage.py test
```

## Environments
There are three distinct environments (dev, test and prod) that can be spawned
with the following commands.

### Test environment
#### Requirements
- docker
- docker-compose
- python 3.x
- pipenv

#### Commands
Start Containers:
```bash
docker-compose -f docker-compose-dev.yml up [-d]
```
Create DB and Seed initial data for tests
```bash
docker-compose -f docker-compose-dev.yml run users python manage.py recreate-db
docker-compose -f docker-compose-dev.yml run users python manage.py seed-db
```
Run tests
```bash
docker-compose -f docker-compose-dev.yml run users python manage.py test
```

### Prod environment
This environment is run on amazon (free tier).
#### Requirements
- docker
- docker-machine
- aws credentials

#### Commands
Intialize docker-machine at amazon ec2:
```bash
docker-machine create --driver amazonec2 testdriven-prod
eval $(docker-machine env testdriven-prod)
```
You can check if the environment is up and running with `docker-machine ls`.

Create docker containers
```bash
docker-compose -f docker-compose-prod.yml up -d --build
```
Create DB and Seed initial data for tests
```bash
docker-compose -f docker-compose-prod.yml run users python manage.py recreate-db
docker-compose -f docker-compose-prod.yml run users python manage.py seed-db
```
Run tests
```bash
docker-compose -f docker-compose-prod.yml run users python manage.py test
```
Check the ip of the ec2 instance `docker-machine ip testdriven-prod`.

## Common commands
Access to the database via psql:
```bash
docker-compose -f docker-compose-dev.yml exec users-db psql -U postgres
```
