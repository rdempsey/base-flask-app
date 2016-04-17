# Base Flask App

## Overview

This project is application skeleton for typical Flask and AngularJS web apps. You can use it to quickly bootstrap your Flask and Angular web app projects and dev environment.

The project contains two things:

1. A sample Flask application configured to serve dynamic pages as well as provide an example API
2. A sample AngularJS application based off [angular-seed](https://github.com/angular/angular-seed) used to interact with the API created using Flask

## What's In The Box - Flask

There's a ton of pre-packaged goodness in the Flask application for you. Here's the list:

### Design

* Fully implemented Bootstrap theme: Readable from [Bootswatch](http://bootswatch.com/readable/)
* Over 250 glyphs in font format from the Glyphicon Halflings set.
* Done-for-you drop-down menus just waiting for you to expand the app and add your own urls.
* Custom favicon made from the Flask logo. Just replace it with yours.

### Javascript

* [jQuery](https://jquery.com/) 2.2.3
* [D3.js](https://d3js.org/) 3.5.16
* [Moment.js](http://momentjs.com/) 2.12.0 - for parsing, validating, manipulating, and displaying dates in JavaScript.
* [BootStrap DateTimePicker](https://github.com/Eonasdan/bootstrap-datetimepicker) 4.17.37 - make your datetime picker look super hot.

### Python

* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](http://flask-restful-cn.readthedocs.org/en/0.3.4/)
* [Scutils](https://github.com/istresearch/scrapy-cluster/tree/master/utils)
* [Markdown](https://pypi.python.org/pypi/Markdown)

## What's In The Box - AngularJS

The AngularJS application is preconfigured to install the Angular framework and a host of development and testing tools. The app does one thing - demonstrates how to interact with a RESTful API.

## Requirements

* Python 2.7+

If you want to run the AngularJS application, you will also need:

* [Node.js](https://nodejs.org/)
* Node Package Manager (npm)
* [Bower](http://bower.io/#install-bower)

## Getting Started

Clone the repo

    git clone https://github.com/rdempsey/base-flask-app

Navigate to the main directory

    cd base-flask-app/api

Install the requirements

    pip install -r requirements.txt


### Run the Flask App

If you would like run the Flask application, do this:

Change into the api directory:

    cd api

Run the Flask app:

    python index.py

Navigate to the home page: [http://localhost:5000](http://localhost:5000)

### Run the AngularJS App

If you would like run the included AngularJS application, perform the steps in the previous section to start the Flask app and then do the following:

Open a second terminal window and navigate to the angular-for-flask directory (in the base-flask-app folder):

    cd base-flask-app/angular-for-flask

Install the required dependencies:

    npm install

Use Bower to install bootstrap (may require sudo):

    bower install bootstrap

Run the application:

    npm start

Browse to the default page: [http://localhost:8000/app](http://localhost:8000/app)