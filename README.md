# Logs Analysis Project

In this project, I work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. 
The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

```
PostgreSQL
Python 2 or above
Psycopg2 for python
```

### Preparation

A step by step series of examples that tell you have to get a development env running

```
1. Clone or download this repository.
2. Unzip to a folder.
```

## Running the tests

This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons on Udacity.

To load the data, cd into the vagrant directory and use the command ```psql -d news -f newsdata.sql```

### After successfully loaded the date. Do include the ```create view``` statements for these views as this program depends on it.


```
CREATE VIEW failure AS
select DATE(time) as date, count(*) as num
from log
where status = '404 NOT FOUND'
Group by date
Order by date;

CREATE VIEW success AS
select DATE(time) as date, count(*) as num
from log
Group by date
Order by date;

CREATE VIEW rate AS
select failure.date , (failure.num::float / success.num::float) * 100 as percentage
from failure, success
where failure.date = success.date
group by success.date, failure.date, failure.num, success.num
order by failure.date;

```

## Sample Output
```
What are the most popular three articles of all time?

	Candidate is jerk, alleges rival - 338647 views

	Bears love berries, alleges bear - 253801 views

	Bad things gone, say good people - 170098 views

Who are the most popular article authors of all time?

	Ursula La Multa - 507594 views

	Rudolf von Treppenwitz - 423457 views

	Anonymous Contributor - 170098 views

	Markoff Chaney - 84557 views

On which days did more than 1% of requests lead to errors

	July 17, 2016 - 2.3% errors

```

## Authors

* **Ong Kuo Han** - *Initial work* - [Kuo Han](https://github.com/kuohan95)
