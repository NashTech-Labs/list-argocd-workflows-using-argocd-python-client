# list-argocd-workflows-using-argocd-python-client

## Argocd
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. ArgoCD is a GitOps continuous delivery tool that means you define all your applications, manifests, and resources that you want to deploy in your Kubernetes cluster, you define all of them in your GitHub repository, and then the ArgoCD will pull the changes from your GitHub repository and deploy resources for you in your Kubernetes cluster.


## Argocd Python Client

For Install Argocd Python Client using following command:

```
$ pip install argo-workflows
```

## Delete Workflow using Argocd Python Client:
For deleting workflow using this python client we need to give our configurations in delete.py file:

```
configuration = argo_workflows.Configuration(host="<YOUR_ARGOCD_SERVER_ENDPOINT>")

```

And you have to give the name and namespace of that workflow which you want to delete:

```
namespace = "<NAMESPACE_OF_ARGOWORKFLOW>"
name= "<NAME_OF_WORKFLOW"
```


```
namespace = "argo"  
name= "awesome-dragon"
```


## Run the python file:

```
$ python3 list.py
```

This will successfully List all the workflows present on your argocd cluster.
