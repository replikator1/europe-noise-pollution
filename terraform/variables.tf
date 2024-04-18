variable "project" {
  description = "Project name"
  default     = "dtc-de-course-412911"
}

variable "region" {
  description = "Region of project"
  default     = "europe-central2-a"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bg_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "europe_noise_pollution_ds"
}

variable "gcs_bucket_name" {
  description = "My Storage Name"
  default     = "dtc-de-course-412911-noise-pollution-bucket"
}

variable "gsc_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}