from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()
subscription_id = "9efad8ab-5255-4241-a804-ca8d2aa346f8"

resource_client = ResourceManagementClient(credential, subscription_id)