@jayfk jayfk Update CHANGELOG.md
.idea	node_modules marked as excluded directory	21 days ago
docs	switch to named docker volumes	5 days ago
hooks	post_get hook removes docs for pycharm if it isn't used	17 days ago
tests	adds simple docker test	3 months ago
{{cookiecutter.repo_name}}	celeryworker and celerybeat missing the correct dockerfile	a day ago
.editorconfig	Update editorconfig to match existing project conventions for 2-space…	7 months ago
.gitattributes	Add .gitattributes file.	2 years ago
.gitignore	Adds celerybeat db to gitignore	3 months ago
.travis.yml	update docker-engine on travis	a month ago
CHANGELOG.md	Update CHANGELOG.md	a day ago
CONTRIBUTING.rst	Write docs on running the test suite with tox, resolve #399	5 months ago
CONTRIBUTORS.rst	Merge pull request #511 from epileptic-fish/features/readme-licence	6 days ago
LICENSE	Wrap all line-length to max 80 chars	11 months ago
README.rst	Dockerfile and Dockerfile-dev moved to compose/django/	21 days ago
cookiecutter.json	use_pycharm variable, post_gen_project hook, {{ cookiecutter.repo_nam…	21 days ago
requirements.txt	update requirements	a month ago
setup.cfg	Add DjangoCookieTestCase	a year ago
setup.py	update requirements	a month ago
tox.ini	Ensure that tox passes on certain environment variables	5 months ago
 README.rst
cookiecutter-django
Requirements Status Build Status 
A Cookiecutter template for Django.

Features

For Django 1.9
Renders Django projects with 100% starting test coverage
Twitter Bootstrap v4.0.0 - alpha
End-to-end via Hitch
AngularJS
12-Factor based settings via django-environ
Optimized development and production settings
Registration via django-allauth
Comes with custom user model ready to go.
Grunt build for compass and livereload
Basic e-mail configurations for sending emails via Mailgun
Media storage using Amazon S3
Docker support using docker-compose for development and production
Procfile for deploying to Heroku
Works with Python 2.7.x or 3.5.x!
Run tests with unittest or py.test!
Optional Integrations

These features can be enabled during initial project setup.

Serve static files from Amazon S3 or Whitenoise
Configuration for Celery
Integration with MailHog for local email testing
Integration with Sentry for error logging
Integration with NewRelic for performance monitoring
Integration with Opbeat for performance monitoring
Constraints

Only maintained 3rd party libraries are used.
PostgreSQL everywhere (9.0+)
Environment variables for configuration (This won't work with Apache/mod_wsgi).
Usage

Let's pretend you want to create a Django project called "redditclone". Rather than using startproject and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter to do all the work.

First, get cookiecutter. Trust me, it's awesome:

$ pip install cookiecutter
Now run it against this repo:

$ cookiecutter https://github.com/pydanny/cookiecutter-django.git
You'll be prompted for some questions, answer them, then it will create a Django project for you.

Warning: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

Warning: repo_name must be a valid Python module name or you will have issues on imports.

It prompts you for questions. Answer them:

Cloning into 'cookiecutter-django'...
remote: Counting objects: 550, done.
remote: Compressing objects: 100% (310/310), done.
remote: Total 550 (delta 283), reused 479 (delta 222)
Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
Resolving deltas: 100% (283/283), done.
project_name [project_name]: Reddit Clone
repo_name [Reddit_Clone]: reddit
author_name [Your Name]: Daniel Greenfeld
email [Your email]: pydanny@gmail.com
description [A short description of the project.]: A reddit clone.
domain_name [example.com]: myreddit.com
version [0.1.0]: 0.0.1
timezone [UTC]:
now [2016/03/01]: 2016/03/05
year [2015]:
use_whitenoise [y]: n
use_celery [n]: y
use_mailhog [n]: n
use_sentry [n]: y
use_newrelic [n]: y
use_opbeat [n]: y
use_pycharm [n]: y
windows [n]: n
use_python2 [n]: y
Select open_source_license:
1 - MIT
2 - BSD
3 - Not open source
Choose from 1, 2, 3 [1]: 1
Enter the project and take a look around:

$ cd reddit/
$ ls
Create a GitHub repo and push it there:

$ git init
$ git add .
$ git commit -m "first awesome commit"
$ git remote add origin git@github.com:pydanny/redditclone.git
$ git push -u origin master
Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For development, see the following for local development:

Developing locally
Developing locally using docker
Articles

Development and Deployment of Cookiecutter-Django via Docker
Development and Deployment of Cookiecutter-Django on Fedora
Support This Project
