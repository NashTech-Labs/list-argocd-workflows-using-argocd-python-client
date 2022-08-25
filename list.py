from pprint import pprint

import requests
import yaml

import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_create_request import (
    IoArgoprojWorkflowV1alpha1WorkflowCreateRequest,
)

configuration = argo_workflows.Configuration(host="https://127.0.0.1:2746")
configuration.verify_ssl = False

api_client = argo_workflows.ApiClient(configuration)

with argo_workflows.ApiClient(configuration) as api_client:
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    namespace = "argo"  
try:
    api_response = api_instance.list_workflows(namespace)
    pprint(api_response)
except argo_workflows.ApiException as e:
    print("Exception when calling WorkflowServiceApi->list_workflows: %s\n" % e)
