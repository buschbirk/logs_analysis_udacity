# Logs Analysis

This project uses a PostgreSQL database to analyse data from a fictional news site.

## Getting Started

These instructions will get you a copy of the project up and running on in a virtual environment. 

### Prerequisites

* Python 3.6
* Vagrant 
* VirtualBox 
* SQL database file in /news folder. File can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Installation instructions for Vagrant and VirtualBox can be found in the Built With section below

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
CREATE VIEW articlelog AS
SELECT author, title FROM log as l
JOIN articles as a
ON l.path LIKE concat('%',a.slug,'%');
```

## Run the program

In your virtual environment:
```
cd news
python3.6 news_log.py
```

## Built With

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Author

* Lasse Alsbirk
