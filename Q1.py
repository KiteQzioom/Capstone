# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM q1_csv;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP VIEW IF EXISTS q1_csv_temp1;
# MAGIC DROP VIEW IF EXISTS q1_csv_temp1;
# MAGIC 
# MAGIC CREATE OR REPLACE TEMPORARY VIEW q1_csv_temp1
# MAGIC AS (
# MAGIC     SELECT business_id, name, state, categories, stars, review_count, REPLACE (ByAppointmentOnly, 'None', 'null') as ByAppointmentOnly
# MAGIC     FROM q1_csv
# MAGIC     );
# MAGIC 
# MAGIC CREATE OR REPLACE TEMPORARY VIEW q1_csv_temp
# MAGIC AS (
# MAGIC     SELECT business_id, name, state, categories, stars, review_count, REPLACE (ByAppointmentOnly, 'null', 'null') as ByAppointmentOnly
# MAGIC     FROM q1_csv_temp1
# MAGIC     )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ByAppointmentOnly, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY ByAppointmentOnly

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT BusinessAcceptsCreditCards, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY BusinessAcceptsCreditCards

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT BikeParking, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY BikeParking

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT RestaurantsPriceRange2, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY RestaurantsPriceRange2

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CoatCheck, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY CoatCheck

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT RestaurantsTakeOut, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY RestaurantsTakeOut

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT RestaurantsDelivery, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY RestaurantsDelivery

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Caters, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY Caters

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT WiFi, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY WiFi

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT WheelchairAccessible, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY WheelchairAccessible

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT HappyHour, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY HappyHour

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT OutdoorSeating, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY OutdoorSeating

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT HasTV, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY HasTV

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT RestaurantsReservations, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY RestaurantsReservations

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DogsAllowed, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY DogsAllowed

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Alcohol, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY Alcohol

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT GoodForKids, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY GoodForKids

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT RestaurantsAttire, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY RestaurantsAttire

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DriveThru, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY DriveThru

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT NoiseLevel, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY NoiseLevel

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT BusinessAcceptsBitcoin, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY BusinessAcceptsBitcoin

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Smoking, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY Smoking

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT BYOB, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY BYOB

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT BYOB, count(business_id), avg(stars)
# MAGIC FROM q1_csv
# MAGIC WHERE categories like '%Coffee%'
# MAGIC GROUP BY BYOB

# COMMAND ----------


