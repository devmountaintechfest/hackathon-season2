SELECT HIRED, DATE('now') AS NOW, DATE('now') - HIRED AS DIFF FROM master WHERE DIFF >= 3;

--
-- WITH test AS (
--     select substr('10-11-2019', 7, 4)  as year
--      , substr('10-11-2019', 4, 2)  as month
--      , substr('10-11-2019', 1, 2)  as date
--      , DATE(substr('10-11-2019', 7, 4)
--     || '-'
--     || substr('10-11-2019', 4, 2)
--     || '-'
--     || substr('10-11-2019', 1, 2)) as HIRE,
--     DATE('now') AS NOW
-- )
-- SELECT *, DATE('now') - HIRE AS DIFF FROM test