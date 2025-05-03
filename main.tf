terraform {
  required_providers {
    azurerm={
        source="hashicorp/azurerm"
        version="3.17.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "9efad8ab-5255-4241-a804-ca8d2aa346f8"
  tenant_id = "c0bb4c97-8ab4-4b34-8e5e-f06523bb2dd6"
  client_id = "3f08bde3-df7a-413e-b7a8-f2f24203a9d8"
  client_secret = "Ftf8Q~dk-fVAdYvFm8L_qaGPXwDQaUEEHE2Fqc-q"
  features {    
  }
}

# Create a random name for the resource group using random_pet
resource "random_pet" "rg_name" {
  prefix = var.resource_group_name_prefix
}

# Create a resource group using the generated random name
resource "azurerm_resource_group" "example" {
  location = var.resource_group_location
  name     = random_pet.rg_name.id
}

variable "resource_group_location" {
  type        = string
  default     = "eastus"
  description = "Location of the resource group."
}

variable "resource_group_name_prefix" {
  type        = string
  default     = "rg"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

output "resource_group_name" {
  value = azurerm_resource_group.example.name
}