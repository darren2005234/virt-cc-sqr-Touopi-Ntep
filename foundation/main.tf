terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }

  required_version = ">=0.13"
}

provider "scaleway" {

}


resource "scaleway_registry_namespace" "registry" {
  name = "${var.project_name}-registry"
}


resource "scaleway_k8s_cluster" "cluster" {
  name    = "${var.project_name}-cluster"
  version = "1.29.1"

  cni                         = "cilium"
  delete_additional_resources = true
}


resource "scaleway_rdb_instance" "database" {
  name          = "${var.project_name}-db"
  node_type     = "db-dev-s"
  engine        = "PostgreSQL-14"
  is_ha_cluster = false
}


resource "scaleway_lb_ip" "lb_ip" {

}


resource "scaleway_domain_record" "dns" {
  dns_zone = "polytech-dijon.kiowy.net"
  name     = "calculatrice-${var.binome_1}-${var.binome_2}"
  type     = "A"
  data     = "0.0.0.0"
  ttl      = 300
}
