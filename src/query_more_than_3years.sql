WITH DevClub AS (SELECT *, STRFTIME('%Y-%m-%d', HIRED) AS new_date
                 FROM master
                 WHERE new_date <= DATE('now', '-3 year')
                   AND POSITION IN ('Airhostess', 'Pilot', 'Steward')
                   AND STATUS = 1
                 ORDER BY new_date DESC)
SELECT *
FROM DevClub