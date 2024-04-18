terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.25.0"
    }
  }
}

provider "google" {
  credentials = "keys/dtc-de-course-412911-67824eda21c0.json"
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "pollution_dataset" {
  dataset_id = var.bg_dataset_name
  location = var.location
}



