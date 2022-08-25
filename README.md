# list-argocd-workflows-using-argocd-python-client

## Argocd
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes that means you define all your applications, manifests, and resources that you want to deploy in your Kubernetes cluster, you define all of them in your GitHub repository, and then the ArgoCD will pull the changes from your GitHub repository and deploy resources for you in your Kubernetes cluster.


## Installing argo-workflows python module

To insatll Argocd Python Client argo-workflows module use the following command:

```
$ pip install argo-workflows
```

## List Workflow using Argocd Python Client:
For listing workflows using this python client we need to give our configurations in our .py file:

```
configuration = argo_workflows.Configuration(host="<YOUR_ARGOCD_SERVER_ENDPOINT>")

```

And you have to give the namespace from where you want the workflows to list:

```
namespace = "<NAMESPACE_OF_ARGOWORKFLOW>"
```


```
namespace = "argo"  
```


## Run the python file:

```
$ python3 list.py
```

This will successfully List all the workflows present on your argocd cluster in the specified namespace.
