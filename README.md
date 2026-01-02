### Hexlet tests and linter status:  
[![Actions Status](https://github.com/farguz/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/farguz/python-project-52/actions)  
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=farguz_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=farguz_python-project-52) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=farguz_python-project-52&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=farguz_python-project-52) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=farguz_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=farguz_python-project-52) 

# Task Manager
A Django-based task management app. Final project from Hexlet Python Backend course.  
Deployed version [here](https://task-manager-by-farguz.onrender.com/) (render.com).

## Features
- Task management (CRUD - create, read, update, delete)
- Label, status management
- User authentication and authorization
- Internationalization support (i18n)

## Used tech stack
- Python
- Django
- Bootstrap 5
- PostgreSQL
- uv
- ruff
- Rollbar
- WhiteNoise 
- python-dotenv

## Setup and Installation
```bash
git clone git@github.com:farguz/python-project-52.git
```  
```bash
make install
```  
```bash
make local-start
```  
App will be available at ```http://127.0.0.1:8000/```