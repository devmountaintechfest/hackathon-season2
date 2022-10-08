WITH DevClub AS (SELECT *, STRFTIME('%Y-%m-%d', HIRED) AS new_date
                 FROM master
                 WHERE new_date <= DATE('now', '-3 year')
                   AND POSITION IN ('Airhostess', 'Pilot', 'Steward')
                   AND STATUS IN (1, 2)
                 ORDER BY new_date DESC)
SELECT *
FROM DevClub WHERE STATUS IN (1, 2);


SELECT * FROM master WHERE STATUS IN (1, 2);

SELECT NATIONALITY FROM master GROUP BY NATIONALITY;

SELECT LOWER(NATIONALITY) FROM master GROUP by NATIONALITY;