### Europe noise pollution project

## Project description
The aim of the project is to investigate the level of noise pollution in European cities. Measurement data is collected from the website: https://archive.sensor.community/, which provides free data from various sensors as part of the Open Environmental Data project. In addition to the sound pollutions we are studying, data on air pollution as well as other meteorological data are also provided.


## Tools
* GCP
* Python
* dbt
* Mage
* Terraform

## Dashboard

## How to run the project?

# Prerequisities
```
- docker
- docker-compose
- terraform
- git
- GCP account
```
# 1. Clone git repo
`git clone WSTAW LINK`
`cd europe-noise-pollution`
`cp dev.env .env`

# 2. Copy your google service account key into two folders: 
- to the main directory
- to the `terraform/keys`

# 3. Set up infrastructure with Terraform
`cd terraform`
* Make appropiate changes in `variables.tf`: 
- `project` - enter your GCP project id
- `gcs_bucket_name"` - enter name of GCS bucket (save it somewhere, we'll need it next steps)
* Make change in `main.tf` file:
- `credentials = "keys/(put your key name here).json"`
After that steps make sure you are in `terraform` directory and:
```
terraform init
terraform plan
terraform apply
```

# 4. Changes in the mage configuration 
With your IDE, go to given folders and make following changes:
1. In the `/mage/io_config.yaml` change line: 
* `GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/(put you google service account key name here).json"`

2. Both in  `/mage/data_exporters/location_data_to_gcs_csv.py` and `mage/data_exporters/pollution_data_to_gcs_parquet.py`, and change line:
* `bucket_name = '(put your bucket name here)'`

3. In the `mage/data_exporters/create_external_bq_tables.sql` for both table declarations change lines: 
* `uris = ['gs://(put your bucket name here)/*.parquet']`
* `uris = ['gs://(put your bucket name here)/*.csv']`

4. Finally for dbt configuration: 
In the `mage/dbt/dbt_pollution/profiles.yml` file: 
* `project: (put your project name here)`
* `keyfile: /home/src/(put you google service account key name here).json`

In the `mage/dbt/dbt_pollution/models/staging/schema.yml`
* `database: (put your project name here)`

# 5. Start docker containers 
`docker-compose up`

# 6. Open Mage UI 
* Open your internet browser and go to http://localhost:6789/
* To run pipeline: 
1. On the left panel click pipeline icon, then choose `main_pipeline` from list
2. Click button `Run@once` and then button `Run now`

Whole procedure can take up to 10 minutes.

3. After succesfully completion, new tables in your BigQuery will appear. 

# 7. From that point you can recreate dashboard with selected BI tool. 
