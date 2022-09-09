-- Databricks notebook source
SELECT *
FROM q2_5_csv

-- COMMAND ----------

SELECT *
FROM q2_5_csv
WHERE categories like '%Coffee%' AND is_open = 1

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW Coffee_state
  AS (
    SELECT state, count(business_id), avg(stars) as avg_rating, avg(review_count)
    FROM q2_5_csv
    WHERE categories like '%Coffee%' AND is_open = 1
    GROUP BY state
    ORDER BY avg_rating
  )

-- COMMAND ----------

SELECT *
FROM Coffee_state

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW Food_state
  AS (
    SELECT state, count(business_id), avg(stars), avg(review_count)
    FROM q2_5_csv
    WHERE categories like '%Food%' AND is_open = 1
    GROUP BY state
  )

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW Business_state
  AS (
    SELECT state, count(business_id), avg(stars) as avg_rating, avg(review_count)
    FROM q2_5_csv
    WHERE is_open = 1
    GROUP BY state
    )

-- COMMAND ----------

SELECT C.state, C.avg_rating as coffee_rating, B.avg_rating as business_rating,  C.avg_rating - B.avg_rating as unbiased_rating
FROM Coffee_state as C FULL JOIN Business_state as B ON C.state = B.state
WHERE C.state is not null AND C.avg_rating is not null AND B.avg_rating is not null
ORDER BY unbiased_rating DESC
