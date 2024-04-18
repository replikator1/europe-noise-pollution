CREATE EXTERNAL TABLE IF NOT EXISTS europe_noise_pollution_ds.sensors_external
  OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dtc-de-course-412911-noise-pollution-bucket/*.parquet']);

CREATE EXTERNAL TABLE IF NOT EXISTS europe_noise_pollution_ds.location_external
  OPTIONS (
  format = 'CSV',
  uris = ['gs://dtc-de-course-412911-noise-pollution-bucket/*.csv']);