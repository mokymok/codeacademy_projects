SELECT 
    state,
    year,
    tempf,
    AVG(tempf) OVER (
      PARTITION BY state
      ORDER BY year
    ) 'running_avg_temp'
FROM
    state_climate;

SELECT
    state,
    year,
    tempf,
    FIRST_VALUE(tempf) OVER(
      PARTITION BY state
      ORDER BY tempf
    ) 'lowest_temp'
FROM 
    state_climate;

SELECT
    state,
    year,
    tempf,
    LAST_VALUE(tempf) OVER(
      PARTITION BY state
      ORDER BY tempf
      RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) 'highest_temp'
FROM 
    state_climate;

SELECT
    state,
    year,
    tempf,
    tempf - LAG(tempf, 1, tempf) OVER(
      PARTITION BY state
      ORDER BY year
    ) AS 'change_in_temp'
FROM
    state_climate;

SELECT
    state,
    year,
    tempf,
    RANK() OVER(
      ORDER BY tempf
    ) AS 'coldest_rank'
FROM
    state_climate;

SELECT
    state,
    year,
    tempf,
    RANK() OVER(
      ORDER BY tempf DESC
    ) AS 'warmest_rank'
FROM  
    state_climate;

SELECT
    state,
    year,
    tempf,
    NTILE(4) OVER(
      PARTITION BY state
      ORDER BY tempf 
    ) as 'temp_quarts'
FROM state_climate;

SELECT
    state,
    year,
    tempf,
    NTILE(5) OVER(
      ORDER BY tempf 
    ) as 'temp_quints'
FROM state_climate;
