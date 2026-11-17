import pulumi
import storage
from pulumi_azure_native import resources

env = pulumi.get_stack()

resource_group = resources.ResourceGroup(
    "rg",
    resource_group_name=f"rg-lab-{env}-bvk",
    tags={"environment": env, "managed-by": "pulumi", "owner": "bvk"},
)

pulumi.export("resource_group", resource_group.name)
pulumi.export("location", resource_group.location)
storage.create_storage(resource_group)
import network
vnet, web_subnet, app_subnet, db_subnet = network.create_network(resource_group)
pulumi.export("vnet_name", vnet.name)
pulumi.export("web_subnet_id", web_subnet.id)
pulumi.export("app_subnet_id", app_subnet.id)
pulumi.export("db_subnet_id", db_subnet.id)
import vm
vm.create_vm(resource_group, web_subnet)
