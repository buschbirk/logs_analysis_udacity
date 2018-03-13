# Logs Analysis

This project uses a Postgres database to analyse data from a fictional news site.

## Getting Started

These instructions will get you a copy of the project up and running on in a virtual environment. 

### Prerequisites

* Python 3.6
* Vagrant 
* VirtualBox 
* SQL database file in /news folder. File can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)

Installation instructions for Vagrant and VirtualBox can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

### Installing

Initialise virtual environment

From your terminal, type:
```
vagrant up
```
When finished, ssh into your virtual environment:

```
vagrant ssh
cd /vagrant
```

Initialise database
```
psql -d news -f news/newsdata.sql
```

## Add view to database

In your virtual environment:
```
psql -d news
```
Type in the following SQL command: 
```
news=> CREATE VIEW articlelog AS
news-> SELECT author, title FROM log as l
news-> JOIN articles as a
news-> ON l.path LIKE concat('%',a.slug,'%');
```

## Run the program

In your virtual environment:
```
cd news
python news_log.py
```

## Built With

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - Dependency Management

## Author

* Lasse Alsbirk
