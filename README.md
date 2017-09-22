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


1. Clone or download this [repository](https://github.com/kuohan95/Virtual-Machine.git).  
2. Unzip to a folder.


## Database load up

This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons on Udacity.

To load the data we need the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), cd into the vagrant directory and use the command ```psql -d news -f newsdata.sql```

Once you have the data loaded into your database, connect to your database using ```psql -d news``` and explore the tables using the ```\dt``` and ```\d``` table commands and select statements. 

For easier way of entering the data provided in the repository an sql script called ```create_views.sql```, you could import the views from the command line by typing: psql ```-d news -f create_views.sql```


### After successfully loaded the data. Do check if the ```create view``` statements for these views as this program depends on it.

```sql
CREATE VIEW failure AS
SELECT DATE(time) AS date, COUNT(*) AS num
FROM log
WHERE status = '404 NOT FOUND'
GROUP by date
ORDER by date;

CREATE VIEW success AS
SELECT DATE(time) AS date, count(*) AS num
FROM log
GROUP BY date
ORDER BY date;

CREATE VIEW rate AS
SELECT failure.date , (failure.num::float / success.num::float) * 100 as percentage
FROM failure, success
WHERE failure.date = success.date
GROUP BY success.date, failure.date, failure.num, success.num
ORDER BY failure.date;

```
## Running python script

After successfully loaded the data run the python script.

1. Navigate to where log_analysis.py is located in vagrant.
2. Run the following command:
```python log_analysis.py```

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
