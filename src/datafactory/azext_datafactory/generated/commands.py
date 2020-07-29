# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_datafactory.generated._client_factory import cf_factory
    datafactory_factory = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._factory_operations#FactoryOperations.{'
        '}',
        client_factory=cf_factory)
    with self.command_group('datafactory factory', datafactory_factory, client_factory=cf_factory,
                            is_experimental=True) as g:
        g.custom_command('list', 'datafactory_factory_list')
        g.custom_show_command('show', 'datafactory_factory_show')
        g.custom_command('create', 'datafactory_factory_create')
        g.custom_command('update', 'datafactory_factory_update')
        g.custom_command('delete', 'datafactory_factory_delete')
        g.custom_command('configure-factory-repo', 'datafactory_factory_configure_factory_repo')
        g.custom_command('get-data-plane-access', 'datafactory_factory_get_data_plane_access')
        g.custom_command('get-git-hub-access-token', 'datafactory_factory_get_git_hub_access_token')

    from azext_datafactory.generated._client_factory import cf_integration_runtime
    datafactory_integration_runtime = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._integration_runtime_operations#Integra'
        'tionRuntimeOperations.{}',
        client_factory=cf_integration_runtime)
    with self.command_group('datafactory integration-runtime', datafactory_integration_runtime,
                            client_factory=cf_integration_runtime, is_experimental=True) as g:
        g.custom_command('list', 'datafactory_integration_runtime_list')
        g.custom_show_command('show', 'datafactory_integration_runtime_show')
        g.custom_command('linked-integration-runtime create', 'datafactory_integration_runtime_linked_integration_runti'
                         'me_create')
        g.custom_command('managed create', 'datafactory_integration_runtime_managed_create')
        g.custom_command('self-hosted create', 'datafactory_integration_runtime_self_hosted_create')
        g.custom_command('update', 'datafactory_integration_runtime_update')
        g.custom_command('delete', 'datafactory_integration_runtime_delete')
        g.custom_command('get-connection-info', 'datafactory_integration_runtime_get_connection_info')
        g.custom_command('get-monitoring-data', 'datafactory_integration_runtime_get_monitoring_data')
        g.custom_command('get-status', 'datafactory_integration_runtime_get_status')
        g.custom_command('list-auth-key', 'datafactory_integration_runtime_list_auth_key')
        g.custom_command('regenerate-auth-key', 'datafactory_integration_runtime_regenerate_auth_key')
        g.custom_command('remove-link', 'datafactory_integration_runtime_remove_link')
        g.custom_command('start', 'datafactory_integration_runtime_start', supports_no_wait=True)
        g.custom_command('stop', 'datafactory_integration_runtime_stop', supports_no_wait=True)
        g.custom_command('sync-credentials', 'datafactory_integration_runtime_sync_credentials')
        g.custom_command('upgrade', 'datafactory_integration_runtime_upgrade')
        g.custom_wait_command('wait', 'datafactory_integration_runtime_show')

    from azext_datafactory.generated._client_factory import cf_integration_runtime_node
    datafactory_integration_runtime_node = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._integration_runtime_node_operations#In'
        'tegrationRuntimeNodeOperations.{}',
        client_factory=cf_integration_runtime_node)
    with self.command_group('datafactory integration-runtime-node', datafactory_integration_runtime_node,
                            client_factory=cf_integration_runtime_node, is_experimental=True) as g:
        g.custom_show_command('show', 'datafactory_integration_runtime_node_show')
        g.custom_command('update', 'datafactory_integration_runtime_node_update')
        g.custom_command('delete', 'datafactory_integration_runtime_node_delete')
        g.custom_command('get-ip-address', 'datafactory_integration_runtime_node_get_ip_address')

    from azext_datafactory.generated._client_factory import cf_linked_service
    datafactory_linked_service = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._linked_service_operations#LinkedServic'
        'eOperations.{}',
        client_factory=cf_linked_service)
    with self.command_group('datafactory linked-service', datafactory_linked_service, client_factory=cf_linked_service,
                            is_experimental=True) as g:
        g.custom_command('list', 'datafactory_linked_service_list')
        g.custom_show_command('show', 'datafactory_linked_service_show')
        g.custom_command('create', 'datafactory_linked_service_create')
        g.generic_update_command('update', setter_arg_name='properties', custom_func_name=''
                                 'datafactory_linked_service_update')
        g.custom_command('delete', 'datafactory_linked_service_delete')

    from azext_datafactory.generated._client_factory import cf_dataset
    datafactory_dataset = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._dataset_operations#DatasetOperations.{'
        '}',
        client_factory=cf_dataset)
    with self.command_group('datafactory dataset', datafactory_dataset, client_factory=cf_dataset,
                            is_experimental=True) as g:
        g.custom_command('list', 'datafactory_dataset_list')
        g.custom_show_command('show', 'datafactory_dataset_show')
        g.custom_command('create', 'datafactory_dataset_create')
        g.generic_update_command('update', setter_arg_name='properties',
                                 custom_func_name='datafactory_dataset_update')
        g.custom_command('delete', 'datafactory_dataset_delete')

    from azext_datafactory.generated._client_factory import cf_pipeline
    datafactory_pipeline = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._pipeline_operations#PipelineOperations'
        '.{}',
        client_factory=cf_pipeline)
    with self.command_group('datafactory pipeline', datafactory_pipeline, client_factory=cf_pipeline,
                            is_experimental=True) as g:
        g.custom_command('list', 'datafactory_pipeline_list')
        g.custom_show_command('show', 'datafactory_pipeline_show')
        g.custom_command('create', 'datafactory_pipeline_create')
        g.generic_update_command('update', setter_arg_name='pipeline', custom_func_name='datafactory_pipeline_update')
        g.custom_command('delete', 'datafactory_pipeline_delete')
        g.custom_command('create-run', 'datafactory_pipeline_create_run')

    from azext_datafactory.generated._client_factory import cf_pipeline_run
    datafactory_pipeline_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._pipeline_run_operations#PipelineRunOpe'
        'rations.{}',
        client_factory=cf_pipeline_run)
    with self.command_group('datafactory pipeline-run', datafactory_pipeline_run, client_factory=cf_pipeline_run,
                            is_experimental=True) as g:
        g.custom_show_command('show', 'datafactory_pipeline_run_show')
        g.custom_command('cancel', 'datafactory_pipeline_run_cancel')
        g.custom_command('query-by-factory', 'datafactory_pipeline_run_query_by_factory')

    from azext_datafactory.generated._client_factory import cf_activity_run
    datafactory_activity_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._activity_run_operations#ActivityRunOpe'
        'rations.{}',
        client_factory=cf_activity_run)
    with self.command_group('datafactory activity-run', datafactory_activity_run, client_factory=cf_activity_run,
                            is_experimental=True) as g:
        g.custom_command('query-by-pipeline-run', 'datafactory_activity_run_query_by_pipeline_run')

    from azext_datafactory.generated._client_factory import cf_trigger
    datafactory_trigger = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._trigger_operations#TriggerOperations.{'
        '}',
        client_factory=cf_trigger)
    with self.command_group('datafactory trigger', datafactory_trigger, client_factory=cf_trigger,
                            is_experimental=True) as g:
        g.custom_command('list', 'datafactory_trigger_list')
        g.custom_show_command('show', 'datafactory_trigger_show')
        g.custom_command('create', 'datafactory_trigger_create')
        g.generic_update_command('update', setter_arg_name='properties',
                                 custom_func_name='datafactory_trigger_update')
        g.custom_command('delete', 'datafactory_trigger_delete')
        g.custom_command('get-event-subscription-status', 'datafactory_trigger_get_event_subscription_status')
        g.custom_command('query-by-factory', 'datafactory_trigger_query_by_factory')
        g.custom_command('start', 'datafactory_trigger_start', supports_no_wait=True)
        g.custom_command('stop', 'datafactory_trigger_stop', supports_no_wait=True)
        g.custom_command('subscribe-to-event', 'datafactory_trigger_subscribe_to_event', supports_no_wait=True)
        g.custom_command('unsubscribe-from-event', 'datafactory_trigger_unsubscribe_from_event',
                         supports_no_wait=True)
        g.custom_wait_command('wait', 'datafactory_trigger_show')

    from azext_datafactory.generated._client_factory import cf_trigger_run
    datafactory_trigger_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._trigger_run_operations#TriggerRunOpera'
        'tions.{}',
        client_factory=cf_trigger_run)
    with self.command_group('datafactory trigger-run', datafactory_trigger_run, client_factory=cf_trigger_run,
                            is_experimental=True) as g:
        g.custom_command('cancel', 'datafactory_trigger_run_cancel')
        g.custom_command('query-by-factory', 'datafactory_trigger_run_query_by_factory')
        g.custom_command('rerun', 'datafactory_trigger_run_rerun')
