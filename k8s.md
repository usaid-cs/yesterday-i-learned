# Cube cuttle

## Concepts

You have a bunch of computers. They can all run code. [Kubernetes distributes containers](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)---running your code---to these computers, and manages them so they run your software.

These computers are called **nodes**, and these nodes add up to form a **cluster**. Inside that cluster is a **master** that coordinates the nodes.

### The master

The master maintains the cluster. It makes sure the cluster is healthy. [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)? You update the cluster's nodes from there.

### The nodes

Each node runs a **kubelet**, which communicates with the master, and Docker, which runs containers.

The minimum node count for production is 3.

[Each node can run more than one pod](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/), and different types of pods at once.

### Pods

[Pods are one or more containers](https://kubernetes.io/docs/concepts/workloads/pods/pod/) and a spec for how to run them. [Pods run on a node.](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)

(Some of these commands may need `--container=(id)` if you have more than one container running in the pod.)

* Get pods: `kubectl get pods` (id, name, age, whether or not it's running)
* Describe pods: `kubectl describe pods` (more info than `get`)
* Get logs from a pod: `kubectl logs (podname)`
    * Note: [`--previous=false`](https://github.com/tektoncd/pipeline/issues/782#issuecomment-854616720) needs to come after namespace (`-n`) and pod (`-p`) arguments.
* Run command in a pod (with one container): `kubectl exec (podname) -- (command, like ls)` (the `--` is necessary whenever you want to give your `ls` some arguments.)
* Run shell in a pod (with one container): `kubectl exec -ti (podname) bash`

## Training

Use [`minikube start`](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/) to start a cluster. It can take some time.

Use `kubectl`, [cube cuttle](https://twitter.com/mjg59/status/1112603958256627713), to mess with that cluster. `kubectl version` will show both client and server versions.

Get nodes: `kubectl get nodes`

## Deployment

[Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/) to tell the cluster master what to do. This deploys your image.

    kubectl create deployment (name) --image=(image):(version)

    # This was the one in the tutorial
    kubectl create deployment \
        kubernetes-bootcamp \
        --image=gcr.io/google-samples/kubernetes-bootcamp:v1

Use `kubectl get deployments` to see what was deployed.

## Interacting with a deployment

Use `kubectl proxy` in a new window to proxy into the environment ("pod") that your deployment is in. It will tell you which port is now open.
Expose your deployment permanently with a **service**.

### Proxy

The proxy has an API endpoint at `http://localhost:(port of the proxy)/api/`


## Services

You can use your nodes to run any pod, including unrelated ones. Use [services](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/) to tell your cluster which pods are part of which "app" you deployed.

* Get services: `kubectl get services`
* "Start a service": [`kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080`](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-interactive/) or `kubectl expose deployment kubernetes-bootcamp --type="NodePort" --port 8080`... for some reason that slash does nothing special.

### `k8s.yaml`

* `&` starts an anchor, and `*` starts an alias. For example, [`&flag Apple` creates an anchor named `flag`](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd), and `*flag` is an alias that reuses the value `Apple`. At the end of the day, both of those fields are `Apple`; you get to reuse the same value in different places.
