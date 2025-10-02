resource "azurerm_resource_group" "example" {
  name     = "fitness-agents"
  location = "West Europe"
}

resource "azurerm_kubernetes_cluster" "example" {
  name                = "fitness-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  private_cluster_enabled = false

  dns_prefix          = "fitnessmultiagent"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size = "Standard_D4_v5"

  }


 
  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }
}

output "client_certificate" {
  value     = azurerm_kubernetes_cluster.example.kube_config[0].client_certificate
  sensitive = true
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.example.kube_config_raw

  sensitive = true
}



provider "azurerm" {
  features {}
  subscription_id = "your_id"
}


