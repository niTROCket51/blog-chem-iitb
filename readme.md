# Chemblog IITB

The Source Code for ChemBlog IITB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To get started you need to have `Python (>=v3.6)` installed. Get it from here:
[Download Python](https://www.python.org/downloads/)

Install `Django` with the command:
```
pip install Django==3.0.5
```
Get `git` from here:
[Download Git](https://git-scm.com/downloads)

### Installing

Now, move to a desired location and use this command to clone this repository
```
git clone https://github.com/niTROCket51/blog-chem-iitb.git
```
Now,
```
cd blog-chem-iitb
```

To create superuser:
```
python manage.py createsuperuser
```
Fill the required fields.<br/>

Start the development server:
```
python manage.py runserver
```
Now visit 127.0.0.1:8000/ in your browser to view the current build.<br/>

Visit 127.0.0.1:8000/admin/ to update the blog.<br/>
Use the info you used while creaing superuser to login.<br/>

RESTful API can be accessed at 127.0.0.1:8000/api/<br/>

## Running the tests

//TODO

## Deployment

//TODO

## Built with
* Python 3.7 - The programming language
* Django 3.0.5 - The web framework
* ~~Jinja2~~ DTL - The template engine

## Contributors

* [moomoodoggo](http://github.com/moomoodoggo)
* [niTROCket51](https://github.com/niTROCket51)
