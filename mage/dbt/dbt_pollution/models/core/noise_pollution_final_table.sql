{{
 config(
   materialized = 'incremental',
   incremental_strategy = 'insert_overwrite',
   partition_by = {
     'field': 'measurement_time', 
     'data_type': 'timestamp',
     'granularity': 'hour'
   }
 )
}}

WITH location AS (
    SELECT DISTINCT
        l.lat AS latitude,
        l.lon AS longitude,
        l.city_name AS city,
        l.country AS country
    FROM {{ ref('stg_location') }} AS l
), sensors AS (
    SELECT
        s.timestamp AS measurement_time,
        s.sensor_type,
        s.lat AS latitude,
        s.lon AS longitude,
        s.noise_LAeq,
        s.noise_LA_min,
        s.noise_LA_max
    FROM {{ ref('stg_sensors_data') }} AS s
)

SELECT
    s.measurement_time,
    s.sensor_type,
    s.latitude,
    s.longitude,
    l.city,
    l.country,
    s.noise_LAeq,
    s.noise_LA_min,
    s.noise_LA_max
FROM
    sensors AS s
LEFT JOIN
    location AS l
ON
    s.latitude = l.latitude AND s.longitude = l.longitude