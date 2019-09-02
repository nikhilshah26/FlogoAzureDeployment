import pytest
from src.aci_docs_sample import *

junit_suite_name = "AzureCLI"

def test_create_container_group():
    azure_region = 'eastus'
    resource_group_name = 'aci-rg-' + ''.join(random.choice(string.digits)
                                              for _ in range(6))
    container_group_name = 'aci-' + ''.join(random.choice(string.digits)
                                            for _ in range(6))

    multi_container_group_name = container_group_name + "-multi"
    task_container_group_name = container_group_name + "-task"

    container_image_app = "microsoft/aci-helloworld"
    container_image_sidecar = "microsoft/aci-tutorial-sidecar"
    container_image_taskbased = "microsoft/aci-wordcount"

    # Authenticate the management clients with Azure.
    # Set the AZURE_AUTH_LOCATION environment variable to the full path to an
    # auth file. Generate an auth file with the Azure CLI or Cloud Shell:
    # az ad sp create-for-rbac --sdk-auth > my.azureauth
    auth_file_path = getenv('AZURE_AUTH_LOCATION', None)
    if auth_file_path is not None:
        print("Authenticating with Azure using credentials in file at {0}"
              .format(auth_file_path))

        aciclient = get_client_from_auth_file(
            ContainerInstanceManagementClient)
        resclient = get_client_from_auth_file(ResourceManagementClient)
    else:
        print("\nFailed to authenticate to Azure. Have you set the"
              " AZURE_AUTH_LOCATION environment variable?\n")

    # Create (and then get) a resource group into which the container groups
    # are to be created
    print("Creating resource group '{0}'...".format(resource_group_name))
    resclient.resource_groups.create_or_update(resource_group_name,
                                               {'location': azure_region})
    resource_group = resclient.resource_groups.get(resource_group_name)

    # Demonstrate various container group operations
    create_container_group(aciclient, resource_group, container_group_name,
                           container_image_app)
    """ yield create_container_group
    print("In teardown")
    aciclient.container_groups.delete(resource_group_name,
                                      container_group_name)
    aciclient.container_groups.delete(resource_group_name,
                                      multi_container_group_name)
    aciclient.container_groups.delete(resource_group_name,
                                      task_container_group_name)
    resclient.resource_groups.delete(resource_group_name) """


def test_list_container_groups():
    pass

def test_print_container_group_details():
    pass

def test_run_task_based_container():
    pass