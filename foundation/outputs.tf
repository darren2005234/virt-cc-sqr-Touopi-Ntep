output "registry_name" {
  value = scaleway_registry_namespace.registry.name
}

output "cluster_name" {
  value = scaleway_k8s_cluster.cluster.name
}
