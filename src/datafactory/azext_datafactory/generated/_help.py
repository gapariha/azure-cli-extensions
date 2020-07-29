# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['datafactory factory'] = """
    type: group
    short-summary: datafactory factory
"""

helps['datafactory factory list'] = """
    type: command
    short-summary: Lists factories under the specified subscription.
    examples:
      - name: Factories_ListByResourceGroup
        text: |-
               az datafactory factory list --resource-group "exampleResourceGroup"
"""

helps['datafactory factory show'] = """
    type: command
    short-summary: Gets a factory.
    examples:
      - name: Factories_Get
        text: |-
               az datafactory factory show --name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory factory create'] = """
    type: command
    short-summary: Creates or updates a factory.
    parameters:
      - name: --factory-vsts-configuration
        short-summary: Factory's VSTS repo information.
        long-summary: |
            Usage: --factory-vsts-configuration project-name=XX tenant-id=XX type=XX account-name=XX \
repository-name=XX collaboration-branch=XX root-folder=XX last-commit-id=XX

            project-name: Required. VSTS project name.
            tenant-id: VSTS tenant id.
            type: Required. Type of repo configuration.
            account-name: Required. Account name.
            repository-name: Required. Repository name.
            collaboration-branch: Required. Collaboration branch.
            root-folder: Required. Root folder.
            last-commit-id: Last commit id.
      - name: --factory-git-hub-configuration
        short-summary: Factory's GitHub repo information.
        long-summary: |
            Usage: --factory-git-hub-configuration host-name=XX type=XX account-name=XX repository-name=XX \
collaboration-branch=XX root-folder=XX last-commit-id=XX

            host-name: GitHub Enterprise host name. For example: https://github.mydomain.com
            type: Required. Type of repo configuration.
            account-name: Required. Account name.
            repository-name: Required. Repository name.
            collaboration-branch: Required. Collaboration branch.
            root-folder: Required. Root folder.
            last-commit-id: Last commit id.
    examples:
      - name: Factories_CreateOrUpdate
        text: |-
               az datafactory factory create --location "East US" --name "exampleFactoryName" --resource-group \
"exampleResourceGroup"
"""

helps['datafactory factory update'] = """
    type: command
    short-summary: Updates a factory.
    examples:
      - name: Factories_Update
        text: |-
               az datafactory factory update --name "exampleFactoryName" --tags exampleTag="exampleValue" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory factory delete'] = """
    type: command
    short-summary: Deletes a factory.
    examples:
      - name: Factories_Delete
        text: |-
               az datafactory factory delete --name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory factory configure-factory-repo'] = """
    type: command
    short-summary: Updates a factory's repo information.
    parameters:
      - name: --factory-vsts-configuration
        short-summary: Factory's VSTS repo information.
        long-summary: |
            Usage: --factory-vsts-configuration project-name=XX tenant-id=XX type=XX account-name=XX \
repository-name=XX collaboration-branch=XX root-folder=XX last-commit-id=XX

            project-name: Required. VSTS project name.
            tenant-id: VSTS tenant id.
            type: Required. Type of repo configuration.
            account-name: Required. Account name.
            repository-name: Required. Repository name.
            collaboration-branch: Required. Collaboration branch.
            root-folder: Required. Root folder.
            last-commit-id: Last commit id.
      - name: --factory-git-hub-configuration
        short-summary: Factory's GitHub repo information.
        long-summary: |
            Usage: --factory-git-hub-configuration host-name=XX type=XX account-name=XX repository-name=XX \
collaboration-branch=XX root-folder=XX last-commit-id=XX

            host-name: GitHub Enterprise host name. For example: https://github.mydomain.com
            type: Required. Type of repo configuration.
            account-name: Required. Account name.
            repository-name: Required. Repository name.
            collaboration-branch: Required. Collaboration branch.
            root-folder: Required. Root folder.
            last-commit-id: Last commit id.
    examples:
      - name: Factories_ConfigureFactoryRepo
        text: |-
               az datafactory factory configure-factory-repo --factory-resource-id "/subscriptions/12345678-1234-1234-1\
234-12345678abc/resourceGroups/exampleResourceGroup/providers/Microsoft.DataFactory/factories/exampleFactoryName" \
--factory-vsts-configuration account-name="ADF" collaboration-branch="master" last-commit-id="" project-name="project" \
repository-name="repo" root-folder="/" tenant-id="" --location "East US"
"""

helps['datafactory factory get-data-plane-access'] = """
    type: command
    short-summary: Get Data Plane access.
    examples:
      - name: Factories_GetDataPlaneAccess
        text: |-
               az datafactory factory get-data-plane-access --name "exampleFactoryName" --access-resource-path "" \
--expire-time "2018-11-10T09:46:20.2659347Z" --permissions "r" --profile-name "DefaultProfile" --start-time \
"2018-11-10T02:46:20.2659347Z" --resource-group "exampleResourceGroup"
"""

helps['datafactory factory get-git-hub-access-token'] = """
    type: command
    short-summary: Get GitHub Access Token.
    examples:
      - name: Factories_GetGitHubAccessToken
        text: |-
               az datafactory factory get-git-hub-access-token --name "exampleFactoryName" --git-hub-access-code \
"some" --git-hub-access-token-base-url "some" --git-hub-client-id "some" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime'] = """
    type: group
    short-summary: datafactory integration-runtime
"""

helps['datafactory integration-runtime list'] = """
    type: command
    short-summary: Lists integration runtimes.
    examples:
      - name: IntegrationRuntimes_ListByFactory
        text: |-
               az datafactory integration-runtime list --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup"
"""

helps['datafactory integration-runtime show'] = """
    type: command
    short-summary: Gets an integration runtime.
    examples:
      - name: IntegrationRuntimes_Get
        text: |-
               az datafactory integration-runtime show --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime linked-integration-runtime'] = """
    type: group
    short-summary: datafactory integration-runtime sub group linked-integration-runtime
"""

helps['datafactory integration-runtime linked-integration-runtime create'] = """
    type: command
    short-summary: Create a linked integration runtime entry in a shared integration runtime.
    examples:
      - name: IntegrationRuntimes_CreateLinkedIntegrationRuntime
        text: |-
               az datafactory integration-runtime linked-integration-runtime create --name \
"bfa92911-9fb6-4fbe-8f23-beae87bc1c83" --location "West US" --data-factory-name "e9955d6d-56ea-4be3-841c-52a12c1a9981" \
--subscription-id "061774c7-4b5a-4159-a55b-365581830283" --factory-name "exampleFactoryName" \
--integration-runtime-name "exampleIntegrationRuntime" --resource-group "exampleResourceGroup" --subscription-id \
"12345678-1234-1234-1234-12345678abc"
"""

helps['datafactory integration-runtime managed'] = """
    type: group
    short-summary: datafactory integration-runtime sub group managed
"""

helps['datafactory integration-runtime managed create'] = """
    type: command
    short-summary: Creates or updates an integration runtime.
"""

helps['datafactory integration-runtime self-hosted'] = """
    type: group
    short-summary: datafactory integration-runtime sub group self-hosted
"""

helps['datafactory integration-runtime self-hosted create'] = """
    type: command
    short-summary: Creates or updates an integration runtime.
    examples:
      - name: IntegrationRuntimes_Create
        text: |-
               az datafactory integration-runtime self-hosted create --factory-name "exampleFactoryName" --description \
"A selfhosted integration runtime" --name "exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime update'] = """
    type: command
    short-summary: Updates an integration runtime.
    examples:
      - name: IntegrationRuntimes_Update
        text: |-
               az datafactory integration-runtime update --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup" --auto-update "Off" --update-delay-offset \
"\\"PT3H\\""
"""

helps['datafactory integration-runtime delete'] = """
    type: command
    short-summary: Deletes an integration runtime.
    examples:
      - name: IntegrationRuntimes_Delete
        text: |-
               az datafactory integration-runtime delete --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-connection-info'] = """
    type: command
    short-summary: Gets the on-premises integration runtime connection information for encrypting the on-premises data \
source credentials.
    examples:
      - name: IntegrationRuntimes_GetConnectionInfo
        text: |-
               az datafactory integration-runtime get-connection-info --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-monitoring-data'] = """
    type: command
    short-summary: Get the integration runtime monitoring data, which includes the monitor data for all the nodes \
under this integration runtime.
    examples:
      - name: IntegrationRuntimes_GetMonitoringData
        text: |-
               az datafactory integration-runtime get-monitoring-data --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-status'] = """
    type: command
    short-summary: Gets detailed status information for an integration runtime.
    examples:
      - name: IntegrationRuntimes_GetStatus
        text: |-
               az datafactory integration-runtime get-status --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime list-auth-key'] = """
    type: command
    short-summary: Retrieves the authentication keys for an integration runtime.
    examples:
      - name: IntegrationRuntimes_ListAuthKeys
        text: |-
               az datafactory integration-runtime list-auth-key --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime regenerate-auth-key'] = """
    type: command
    short-summary: Regenerates the authentication key for an integration runtime.
    examples:
      - name: IntegrationRuntimes_RegenerateAuthKey
        text: |-
               az datafactory integration-runtime regenerate-auth-key --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --key-name "authKey2" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime remove-link'] = """
    type: command
    short-summary: Remove all linked integration runtimes under specific data factory in a self-hosted integration \
runtime.
    examples:
      - name: IntegrationRuntimes_Upgrade
        text: |-
               az datafactory integration-runtime remove-link --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --linked-factory-name "exampleFactoryName-linked" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime start'] = """
    type: command
    short-summary: Starts a ManagedReserved type integration runtime.
    examples:
      - name: IntegrationRuntimes_Start
        text: |-
               az datafactory integration-runtime start --factory-name "exampleFactoryName" --name \
"exampleManagedIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime stop'] = """
    type: command
    short-summary: Stops a ManagedReserved type integration runtime.
    examples:
      - name: IntegrationRuntimes_Stop
        text: |-
               az datafactory integration-runtime stop --factory-name "exampleFactoryName" --name \
"exampleManagedIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime sync-credentials'] = """
    type: command
    short-summary: Force the integration runtime to synchronize credentials across integration runtime nodes, and this \
will override the credentials across all worker nodes with those available on the dispatcher node. If you already have \
the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime \
node than using this API directly.
    examples:
      - name: IntegrationRuntimes_SyncCredentials
        text: |-
               az datafactory integration-runtime sync-credentials --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime upgrade'] = """
    type: command
    short-summary: Upgrade self-hosted integration runtime to latest version if availability.
    examples:
      - name: IntegrationRuntimes_Upgrade
        text: |-
               az datafactory integration-runtime upgrade --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datafactory integration-runtime is met.
    examples:
      - name: Pause executing next line of CLI script until the datafactory integration-runtime is successfully \
created.
        text: |-
               az datafactory integration-runtime wait --factory-name "exampleFactoryName" --name \
"exampleIntegrationRuntime" --resource-group "exampleResourceGroup" --created
"""

helps['datafactory integration-runtime-node'] = """
    type: group
    short-summary: datafactory integration-runtime-node
"""

helps['datafactory integration-runtime-node show'] = """
    type: command
    short-summary: Gets a self-hosted integration runtime node.
    examples:
      - name: IntegrationRuntimeNodes_Get
        text: |-
               az datafactory integration-runtime-node show --factory-name "exampleFactoryName" \
--integration-runtime-name "exampleIntegrationRuntime" --node-name "Node_1" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime-node update'] = """
    type: command
    short-summary: Updates a self-hosted integration runtime node.
    examples:
      - name: IntegrationRuntimeNodes_Update
        text: |-
               az datafactory integration-runtime-node update --factory-name "exampleFactoryName" \
--integration-runtime-name "exampleIntegrationRuntime" --node-name "Node_1" --resource-group "exampleResourceGroup" \
--concurrent-jobs-limit 2
"""

helps['datafactory integration-runtime-node delete'] = """
    type: command
    short-summary: Deletes a self-hosted integration runtime node.
    examples:
      - name: IntegrationRuntimesNodes_Delete
        text: |-
               az datafactory integration-runtime-node delete --factory-name "exampleFactoryName" \
--integration-runtime-name "exampleIntegrationRuntime" --node-name "Node_1" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime-node get-ip-address'] = """
    type: command
    short-summary: Get the IP address of self-hosted integration runtime node.
    examples:
      - name: IntegrationRuntimeNodes_GetIpAddress
        text: |-
               az datafactory integration-runtime-node get-ip-address --factory-name "exampleFactoryName" \
--integration-runtime-name "exampleIntegrationRuntime" --node-name "Node_1" --resource-group "exampleResourceGroup"
"""

helps['datafactory linked-service'] = """
    type: group
    short-summary: datafactory linked-service
"""

helps['datafactory linked-service list'] = """
    type: command
    short-summary: Lists linked services.
    examples:
      - name: LinkedServices_ListByFactory
        text: |-
               az datafactory linked-service list --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup"
"""

helps['datafactory linked-service show'] = """
    type: command
    short-summary: Gets a linked service.
    examples:
      - name: LinkedServices_Get
        text: |-
               az datafactory linked-service show --factory-name "exampleFactoryName" --name "exampleLinkedService" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory linked-service create'] = """
    type: command
    short-summary: Creates or updates a linked service.
    examples:
      - name: LinkedServices_Create
        text: |-
               az datafactory linked-service create --factory-name "exampleFactoryName" --properties \
"{\\"type\\":\\"AzureStorage\\",\\"typeProperties\\":{\\"connectionString\\":{\\"type\\":\\"SecureString\\",\\"value\\"\
:\\"DefaultEndpointsProtocol=https;AccountName=examplestorageaccount;AccountKey=<storage key>\\"}}}" --name \
"exampleLinkedService" --resource-group "exampleResourceGroup"
"""

helps['datafactory linked-service update'] = """
    type: command
    short-summary: Creates or updates a linked service.
    examples:
      - name: LinkedServices_Update
        text: |-
               az datafactory linked-service update --factory-name "exampleFactoryName" --properties \
"{\\"type\\":\\"AzureStorage\\",\\"description\\":\\"Example description\\",\\"typeProperties\\":{\\"connectionString\\\
":{\\"type\\":\\"SecureString\\",\\"value\\":\\"DefaultEndpointsProtocol=https;AccountName=examplestorageaccount;Accoun\
tKey=<storage key>\\"}}}" --name "exampleLinkedService" --resource-group "exampleResourceGroup"
"""

helps['datafactory linked-service delete'] = """
    type: command
    short-summary: Deletes a linked service.
    examples:
      - name: LinkedServices_Delete
        text: |-
               az datafactory linked-service delete --factory-name "exampleFactoryName" --name "exampleLinkedService" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory dataset'] = """
    type: group
    short-summary: datafactory dataset
"""

helps['datafactory dataset list'] = """
    type: command
    short-summary: Lists datasets.
    examples:
      - name: Datasets_ListByFactory
        text: |-
               az datafactory dataset list --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory dataset show'] = """
    type: command
    short-summary: Gets a dataset.
    examples:
      - name: Datasets_Get
        text: |-
               az datafactory dataset show --name "exampleDataset" --factory-name "exampleFactoryName" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory dataset create'] = """
    type: command
    short-summary: Creates or updates a dataset.
    examples:
      - name: Datasets_Create
        text: |-
               az datafactory dataset create --properties "{\\"type\\":\\"AzureBlob\\",\\"linkedServiceName\\":{\\"type\
\\":\\"LinkedServiceReference\\",\\"referenceName\\":\\"exampleLinkedService\\"},\\"parameters\\":{\\"MyFileName\\":{\\\
"type\\":\\"String\\"},\\"MyFolderPath\\":{\\"type\\":\\"String\\"}},\\"typeProperties\\":{\\"format\\":{\\"type\\":\\"\
TextFormat\\"},\\"fileName\\":{\\"type\\":\\"Expression\\",\\"value\\":\\"@dataset().MyFileName\\"},\\"folderPath\\":{\
\\"type\\":\\"Expression\\",\\"value\\":\\"@dataset().MyFolderPath\\"}}}" --name "exampleDataset" --factory-name \
"exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory dataset update'] = """
    type: command
    short-summary: Creates or updates a dataset.
    examples:
      - name: Datasets_Update
        text: |-
               az datafactory dataset update --properties "{\\"type\\":\\"AzureBlob\\",\\"description\\":\\"Example \
description\\",\\"linkedServiceName\\":{\\"type\\":\\"LinkedServiceReference\\",\\"referenceName\\":\\"exampleLinkedSer\
vice\\"},\\"parameters\\":{\\"MyFileName\\":{\\"type\\":\\"String\\"},\\"MyFolderPath\\":{\\"type\\":\\"String\\"}},\\"\
typeProperties\\":{\\"format\\":{\\"type\\":\\"TextFormat\\"},\\"fileName\\":{\\"type\\":\\"Expression\\",\\"value\\":\
\\"@dataset().MyFileName\\"},\\"folderPath\\":{\\"type\\":\\"Expression\\",\\"value\\":\\"@dataset().MyFolderPath\\"}}}\
" --name "exampleDataset" --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory dataset delete'] = """
    type: command
    short-summary: Deletes a dataset.
    examples:
      - name: Datasets_Delete
        text: |-
               az datafactory dataset delete --name "exampleDataset" --factory-name "exampleFactoryName" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory pipeline'] = """
    type: group
    short-summary: datafactory pipeline
"""

helps['datafactory pipeline list'] = """
    type: command
    short-summary: Lists pipelines.
    examples:
      - name: Pipelines_ListByFactory
        text: |-
               az datafactory pipeline list --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup"
"""

helps['datafactory pipeline show'] = """
    type: command
    short-summary: Gets a pipeline.
    examples:
      - name: Pipelines_Get
        text: |-
               az datafactory pipeline show --factory-name "exampleFactoryName" --name "examplePipeline" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory pipeline create'] = """
    type: command
    short-summary: Creates or updates a pipeline.
    examples:
      - name: Pipelines_Create
        text: |-
               az datafactory pipeline create --factory-name "exampleFactoryName" --pipeline \
"{\\"activities\\":[{\\"name\\":\\"ExampleForeachActivity\\",\\"type\\":\\"ForEach\\",\\"typeProperties\\":{\\"activiti\
es\\":[{\\"name\\":\\"ExampleCopyActivity\\",\\"type\\":\\"Copy\\",\\"inputs\\":[{\\"type\\":\\"DatasetReference\\",\\"\
parameters\\":{\\"MyFileName\\":\\"examplecontainer.csv\\",\\"MyFolderPath\\":\\"examplecontainer\\"},\\"referenceName\
\\":\\"exampleDataset\\"}],\\"outputs\\":[{\\"type\\":\\"DatasetReference\\",\\"parameters\\":{\\"MyFileName\\":{\\"typ\
e\\":\\"Expression\\",\\"value\\":\\"@item()\\"},\\"MyFolderPath\\":\\"examplecontainer\\"},\\"referenceName\\":\\"exam\
pleDataset\\"}],\\"typeProperties\\":{\\"dataIntegrationUnits\\":32,\\"sink\\":{\\"type\\":\\"BlobSink\\"},\\"source\\"\
:{\\"type\\":\\"BlobSource\\"}}}],\\"isSequential\\":true,\\"items\\":{\\"type\\":\\"Expression\\",\\"value\\":\\"@pipe\
line().parameters.OutputBlobNameList\\"}}}],\\"parameters\\":{\\"JobId\\":{\\"type\\":\\"String\\"},\\"OutputBlobNameLi\
st\\":{\\"type\\":\\"Array\\"}},\\"variables\\":{\\"TestVariableArray\\":{\\"type\\":\\"Array\\"}},\\"runDimensions\\":\
{\\"JobId\\":{\\"type\\":\\"Expression\\",\\"value\\":\\"@pipeline().parameters.JobId\\"}}}" --name "examplePipeline" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory pipeline update'] = """
    type: command
    short-summary: Creates or updates a pipeline.
    examples:
      - name: Pipelines_Update
        text: |-
               az datafactory pipeline update --factory-name "exampleFactoryName" --description "Example description" \
--activities "[{\\"name\\":\\"ExampleForeachActivity\\",\\"type\\":\\"ForEach\\",\\"typeProperties\\":{\\"activities\\"\
:[{\\"name\\":\\"ExampleCopyActivity\\",\\"type\\":\\"Copy\\",\\"inputs\\":[{\\"type\\":\\"DatasetReference\\",\\"param\
eters\\":{\\"MyFileName\\":\\"examplecontainer.csv\\",\\"MyFolderPath\\":\\"examplecontainer\\"},\\"referenceName\\":\\\
"exampleDataset\\"}],\\"outputs\\":[{\\"type\\":\\"DatasetReference\\",\\"parameters\\":{\\"MyFileName\\":{\\"type\\":\
\\"Expression\\",\\"value\\":\\"@item()\\"},\\"MyFolderPath\\":\\"examplecontainer\\"},\\"referenceName\\":\\"exampleDa\
taset\\"}],\\"typeProperties\\":{\\"dataIntegrationUnits\\":32,\\"sink\\":{\\"type\\":\\"BlobSink\\"},\\"source\\":{\\"\
type\\":\\"BlobSource\\"}}}],\\"isSequential\\":true,\\"items\\":{\\"type\\":\\"Expression\\",\\"value\\":\\"@pipeline(\
).parameters.OutputBlobNameList\\"}}}]" --parameters "{\\"OutputBlobNameList\\":{\\"type\\":\\"Array\\"}}" --name \
"examplePipeline" --resource-group "exampleResourceGroup"
"""

helps['datafactory pipeline delete'] = """
    type: command
    short-summary: Deletes a pipeline.
    examples:
      - name: Pipelines_Delete
        text: |-
               az datafactory pipeline delete --factory-name "exampleFactoryName" --name "examplePipeline" \
--resource-group "exampleResourceGroup"
"""

helps['datafactory pipeline create-run'] = """
    type: command
    short-summary: Creates a run of a pipeline.
    examples:
      - name: Pipelines_CreateRun
        text: |-
               az datafactory pipeline create-run --factory-name "exampleFactoryName" --parameters \
"{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]}" --name "examplePipeline" --resource-group \
"exampleResourceGroup"
"""

helps['datafactory pipeline-run'] = """
    type: group
    short-summary: datafactory pipeline-run
"""

helps['datafactory pipeline-run show'] = """
    type: command
    short-summary: Get a pipeline run by its run ID.
    examples:
      - name: PipelineRuns_Get
        text: |-
               az datafactory pipeline-run show --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --run-id "2f7fdb90-5df1-4b8e-ac2f-064cfa58202b"
"""

helps['datafactory pipeline-run cancel'] = """
    type: command
    short-summary: Cancel a pipeline run by its run ID.
    examples:
      - name: PipelineRuns_Cancel
        text: |-
               az datafactory pipeline-run cancel --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --run-id "16ac5348-ff82-4f95-a80d-638c1d47b721"
"""

helps['datafactory pipeline-run query-by-factory'] = """
    type: command
    short-summary: Query pipeline runs in the factory based on input filter conditions.
    parameters:
      - name: --filters
        short-summary: List of filters.
        long-summary: |
            Usage: --filters operand=XX operator=XX values=XX

            operand: Required. Parameter name to be used for filter. The allowed operands to query pipeline runs are \
PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName, ActivityRunStart, ActivityRunEnd, \
ActivityType and Status, and to query trigger runs are TriggerName, TriggerRunTimestamp and Status.
            operator: Required. Operator to be used for filter.
            values: Required. List of filter values.

            Multiple actions can be specified by using more than one --filters argument.
      - name: --order-by
        short-summary: List of OrderBy option.
        long-summary: |
            Usage: --order-by order-by=XX order=XX

            order-by: Required. Parameter name to be used for order by. The allowed parameters to order by for \
pipeline runs are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName, ActivityRunStart, \
ActivityRunEnd and Status; for trigger runs are TriggerName, TriggerRunTimestamp and Status.
            order: Required. Sorting order of the parameter.

            Multiple actions can be specified by using more than one --order-by argument.
    examples:
      - name: PipelineRuns_QueryByFactory
        text: |-
               az datafactory pipeline-run query-by-factory --factory-name "exampleFactoryName" --filters \
operand="PipelineName" operator="Equals" values="examplePipeline" --last-updated-after "2018-06-16T00:36:44.3345758Z" \
--last-updated-before "2018-06-16T00:49:48.3686473Z" --resource-group "exampleResourceGroup"
"""

helps['datafactory activity-run'] = """
    type: group
    short-summary: datafactory activity-run
"""

helps['datafactory activity-run query-by-pipeline-run'] = """
    type: command
    short-summary: Query activity runs based on input filter conditions.
    parameters:
      - name: --filters
        short-summary: List of filters.
        long-summary: |
            Usage: --filters operand=XX operator=XX values=XX

            operand: Required. Parameter name to be used for filter. The allowed operands to query pipeline runs are \
PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName, ActivityRunStart, ActivityRunEnd, \
ActivityType and Status, and to query trigger runs are TriggerName, TriggerRunTimestamp and Status.
            operator: Required. Operator to be used for filter.
            values: Required. List of filter values.

            Multiple actions can be specified by using more than one --filters argument.
      - name: --order-by
        short-summary: List of OrderBy option.
        long-summary: |
            Usage: --order-by order-by=XX order=XX

            order-by: Required. Parameter name to be used for order by. The allowed parameters to order by for \
pipeline runs are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName, ActivityRunStart, \
ActivityRunEnd and Status; for trigger runs are TriggerName, TriggerRunTimestamp and Status.
            order: Required. Sorting order of the parameter.

            Multiple actions can be specified by using more than one --order-by argument.
    examples:
      - name: ActivityRuns_QueryByPipelineRun
        text: |-
               az datafactory activity-run query-by-pipeline-run --factory-name "exampleFactoryName" \
--last-updated-after "2018-06-16T00:36:44.3345758Z" --last-updated-before "2018-06-16T00:49:48.3686473Z" \
--resource-group "exampleResourceGroup" --run-id "2f7fdb90-5df1-4b8e-ac2f-064cfa58202b"
"""

helps['datafactory trigger'] = """
    type: group
    short-summary: datafactory trigger
"""

helps['datafactory trigger list'] = """
    type: command
    short-summary: Lists triggers.
    examples:
      - name: Triggers_ListByFactory
        text: |-
               az datafactory trigger list --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger show'] = """
    type: command
    short-summary: Gets a trigger.
    examples:
      - name: Triggers_Get
        text: |-
               az datafactory trigger show --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger"
"""

helps['datafactory trigger create'] = """
    type: command
    short-summary: Creates or updates a trigger.
    examples:
      - name: Triggers_Create
        text: |-
               az datafactory trigger create --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{\\"parameters\\":{\\"OutputBlo\
bNameList\\":[\\"exampleoutput.csv\\"]},\\"pipelineReference\\":{\\"type\\":\\"PipelineReference\\",\\"referenceName\\"\
:\\"examplePipeline\\"}}],\\"typeProperties\\":{\\"recurrence\\":{\\"endTime\\":\\"2018-06-16T00:55:13.8441801Z\\",\\"f\
requency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:13.8441801Z\\",\\"timeZone\\":\\"UTC\\"}}\
}" --name "exampleTrigger"
"""

helps['datafactory trigger update'] = """
    type: command
    short-summary: Creates or updates a trigger.
    examples:
      - name: Triggers_Update
        text: |-
               az datafactory trigger update --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"description\\":\\"Example \
description\\",\\"pipelines\\":[{\\"parameters\\":{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]},\\"pipelineRefer\
ence\\":{\\"type\\":\\"PipelineReference\\",\\"referenceName\\":\\"examplePipeline\\"}}],\\"typeProperties\\":{\\"recur\
rence\\":{\\"endTime\\":\\"2018-06-16T00:55:14.905167Z\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\"\
:\\"2018-06-16T00:39:14.905167Z\\",\\"timeZone\\":\\"UTC\\"}}}" --name "exampleTrigger"
"""

helps['datafactory trigger delete'] = """
    type: command
    short-summary: Deletes a trigger.
    examples:
      - name: Triggers_Delete
        text: |-
               az datafactory trigger delete --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger get-event-subscription-status'] = """
    type: command
    short-summary: Get a trigger's event subscription status.
    examples:
      - name: Triggers_GetEventSubscriptionStatus
        text: |-
               az datafactory trigger get-event-subscription-status --factory-name "exampleFactoryName" \
--resource-group "exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger query-by-factory'] = """
    type: command
    short-summary: Query triggers.
    examples:
      - name: Triggers_QueryByFactory
        text: |-
               az datafactory trigger query-by-factory --factory-name "exampleFactoryName" --parent-trigger-name \
"exampleTrigger" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger start'] = """
    type: command
    short-summary: Starts a trigger.
    examples:
      - name: Triggers_Start
        text: |-
               az datafactory trigger start --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger stop'] = """
    type: command
    short-summary: Stops a trigger.
    examples:
      - name: Triggers_Stop
        text: |-
               az datafactory trigger stop --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger"
"""

helps['datafactory trigger subscribe-to-event'] = """
    type: command
    short-summary: Subscribe event trigger to events.
    examples:
      - name: Triggers_SubscribeToEvents
        text: |-
               az datafactory trigger subscribe-to-event --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger unsubscribe-from-event'] = """
    type: command
    short-summary: Unsubscribe event trigger from events.
    examples:
      - name: Triggers_UnsubscribeFromEvents
        text: |-
               az datafactory trigger unsubscribe-from-event --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datafactory trigger is met.
    examples:
      - name: Pause executing next line of CLI script until the datafactory trigger is successfully created.
        text: |-
               az datafactory trigger wait --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger" --created
"""

helps['datafactory trigger-run'] = """
    type: group
    short-summary: datafactory trigger-run
"""

helps['datafactory trigger-run cancel'] = """
    type: command
    short-summary: Cancel a single trigger instance by runId.
    examples:
      - name: Triggers_Rerun
        text: |-
               az datafactory trigger-run cancel --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --run-id "2f7fdb90-5df1-4b8e-ac2f-064cfa58202b" --trigger-name "exampleTrigger"
"""

helps['datafactory trigger-run query-by-factory'] = """
    type: command
    short-summary: Query trigger runs.
    parameters:
      - name: --filters
        short-summary: List of filters.
        long-summary: |
            Usage: --filters operand=XX operator=XX values=XX

            operand: Required. Parameter name to be used for filter. The allowed operands to query pipeline runs are \
PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName, ActivityRunStart, ActivityRunEnd, \
ActivityType and Status, and to query trigger runs are TriggerName, TriggerRunTimestamp and Status.
            operator: Required. Operator to be used for filter.
            values: Required. List of filter values.

            Multiple actions can be specified by using more than one --filters argument.
      - name: --order-by
        short-summary: List of OrderBy option.
        long-summary: |
            Usage: --order-by order-by=XX order=XX

            order-by: Required. Parameter name to be used for order by. The allowed parameters to order by for \
pipeline runs are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName, ActivityRunStart, \
ActivityRunEnd and Status; for trigger runs are TriggerName, TriggerRunTimestamp and Status.
            order: Required. Sorting order of the parameter.

            Multiple actions can be specified by using more than one --order-by argument.
    examples:
      - name: TriggerRuns_QueryByFactory
        text: |-
               az datafactory trigger-run query-by-factory --factory-name "exampleFactoryName" --filters \
operand="TriggerName" operator="Equals" values="exampleTrigger" --last-updated-after "2018-06-16T00:36:44.3345758Z" \
--last-updated-before "2018-06-16T00:49:48.3686473Z" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger-run rerun'] = """
    type: command
    short-summary: Rerun single trigger instance by runId.
    examples:
      - name: Triggers_Rerun
        text: |-
               az datafactory trigger-run rerun --factory-name "exampleFactoryName" --resource-group \
"exampleResourceGroup" --run-id "2f7fdb90-5df1-4b8e-ac2f-064cfa58202b" --trigger-name "exampleTrigger"
"""
