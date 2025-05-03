from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()
subscription_id = "9efad8ab-5255-4241-a804-ca8d2aa346f8"

resource_client = ResourceManagementClient(credential, subscription_id)

rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg", {"location": "centralus"}
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")
