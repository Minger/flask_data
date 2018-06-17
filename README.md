# Flask Data

## Motivation

This is a few hours effort to learn enough Flask and SqlAlchemy to set up an dockerized server that slurps a csv file into PostgreSQL and serves an arbitrarily chosen field from a row found by primary key. This effort relies on pandas to "automagically" create an sql table from csv and then on SqlAlchemy to create a class from sql table. (In production, one should define these things manually, especially for domain models--I've seen bugs due to unexpected results from such automapping.) One hitch in this process was the table not being viable for SqlAlchemy AutoMapping due to lack of a primary index, which was easily remedied once understood. (We would have thought of this up front had we handrolled the schema.)

I got this working with the native SqlAlchemy library rather than the Flask-SqlAlchemy extension. I suspect the latter would work just as well with the solution to the viable table issue--and would be the desired path for a production Flask application.

Having been working with a statically typed language for the past year or so, it was slightly disorienting coming back to a dynamically typed language without the IDE hints. The flask debugger is useful for inspecting objects and running statements in context like Ruby's pry.

## Making a request

1. Start the service:

   `docker-compose up --build`

2. Pick a policyid from the csv:

   `GET http://127.0.0.1:5000/insurance/119736`

   See `CLAY COUNTY`