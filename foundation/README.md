# Fondation - Terraform (Scaleway)

## Description
Cette partie décrit l'infrastructure Cloud de la calculatrice cloud native,
déployée chez Scaleway via Terraform.

## Ressources créés mais non déployées
- Registre de conteneurs
- Cluster Kubernetes
- Bases de données (dev / prod)
- LoadBalancers (dev / prod)
- Entrées DNS


# Infrastructure Terraform – Scaleway

## Variables utilisées

- binome_1 : Marie
- binome_2 : Darren

## Commande exécutée

```bash
terraform plan -var="binome_1=Marie" -var="binome_2=Darren"


## Résultat du terraform plan


Terraform used the selected providers to generate the following     
execution plan. Resource actions are indicated with the following   
symbols:
  + create

Terraform will perform the following actions:

  # scaleway_domain_record.dns will be created
  + resource "scaleway_domain_record" "dns" {
      + data       = "0.0.0.0"
      + dns_zone   = "polytech-dijon.kiowy.net"
      + fqdn       = (known after apply)
      + id         = (known after apply)
      + name       = "calculatrice-Marie-Darren"
      + priority   = (known after apply)
      + project_id = (known after apply)
      + root_zone  = (known after apply)
      + ttl        = 300
      + type       = "A"
    }

  # scaleway_k8s_cluster.cluster will be created
  + resource "scaleway_k8s_cluster" "cluster" {
      + apiserver_url               = (known after apply)
      + cni                         = "cilium"
      + created_at                  = (known after apply)
      + delete_additional_resources = true
      + id                          = (known after apply)
      + kubeconfig                  = (sensitive value)
      + name                        = "calculatrice-cluster"        
      + organization_id             = (known after apply)
      + pod_cidr                    = (known after apply)
      + project_id                  = (known after apply)
      + service_cidr                = (known after apply)
      + service_dns_ip              = (known after apply)
      + status                      = (known after apply)
      + type                        = (known after apply)
      + updated_at                  = (known after apply)
      + upgrade_available           = (known after apply)
      + version                     = "1.29.1"
      + wildcard_dns                = (known after apply)

      + auto_upgrade (known after apply)

      + autoscaler_config (known after apply)

      + open_id_connect_config (known after apply)
    }

  # scaleway_lb_ip.lb_ip will be created
  + resource "scaleway_lb_ip" "lb_ip" {
      + id              = (known after apply)
      + ip_address      = (known after apply)
      + is_ipv6         = false
      + lb_id           = (known after apply)
      + organization_id = (known after apply)
      + project_id      = (known after apply)
      + region          = (known after apply)
      + reverse         = (known after apply)
    }

  # scaleway_rdb_instance.database will be created
  + resource "scaleway_rdb_instance" "database" {
      + backup_same_region        = (known after apply)
      + backup_schedule_frequency = (known after apply)
      + backup_schedule_retention = (known after apply)
      + certificate               = (known after apply)
      + disable_backup            = false
      + endpoint_ip               = (known after apply)
      + endpoint_port             = (known after apply)
      + engine                    = "PostgreSQL-14"
      + id                        = (known after apply)
      + is_ha_cluster             = false
      + name                      = "calculatrice-db"
      + node_type                 = "db-dev-s"
      + organization_id           = (known after apply)
      + project_id                = (known after apply)
      + read_replicas             = (known after apply)
      + settings                  = (known after apply)
      + upgradable_versions       = (known after apply)
      + user_name                 = (known after apply)
      + volume_size_in_gb         = (known after apply)
      + volume_type               = "lssd"

      + logs_policy (known after apply)

      + private_ip (known after apply)
    }

  # scaleway_registry_namespace.registry will be created
  + resource "scaleway_registry_namespace" "registry" {
      + endpoint        = (known after apply)
      + id              = (known after apply)
      + name            = "calculatrice-registry"
      + organization_id = (known after apply)
      + project_id      = (known after apply)
    }

Plan: 5 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + cluster_name  = "calculatrice-cluster"
  + registry_name = "calculatrice-registry"

─────────────────────────────────────────────────────────────────── 

Note: You didn't use the -out option to save this plan, so
Terraform can't guarantee to take exactly these actions if you run  
"terraform apply" now.
