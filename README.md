# Microservices using Python [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20this%20cool%20project&url=https://github.com/Cool/Project&hashtags=project,opensource)

![Screenshot_2022-01-31_00-41-21](https://user-images.githubusercontent.com/46785329/151713925-6ee37d70-ea28-432e-818b-12759fa06c72.png)

#### This project is an attempt to show that how microservices works using python.

## Table of content

- [**Getting Started**](#getting-started)
- [Built With](#built-with)
- [Contributing](#contributing)
- [Get Help](#get-help)

## Getting Started

### Setup
To create virtual evironment
```console
$ sudo apt-get install python-pip
$ sudo pip install virtualenvwrapper
$ mkvirtualenv env
$ workon env
```
To install all the dependencies:
```console
(env)$ pip install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

To run the application simply type
```console
(env)$ sudo docker-compose up
(env)$ sudo docker-compose exec backend sh
>> python manage.py makemigrations
>> python manage.py migrate
```

## Built With

To build this application used Django framework with postgresql & also use rabbitmq after that I dockerize this application.

## Contributing

#### Issues
In the case of a bug report, bugfix or a suggestions, please feel very free to open an issue.

#### Pull request
Pull requests are always welcome, and I'll do my best to do reviews as fast as I can.

## Get Help
- Contact me on harshalhiwarkar01@gmail.com
- If appropriate, [open an issue](https://github.com/this/project/issues) on GitHub
