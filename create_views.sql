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
