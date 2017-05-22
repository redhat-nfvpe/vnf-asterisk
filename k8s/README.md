# vnf-asterisk under Kubernetes

Here's a series of instructions of how to get vnf-asterisk running under k8s.

## Catalog

* `preload.yml` : preload images on the boxen
* `labels.yml` : assign labels to kube nodes
* `load_podspec.yml` : load podspec(s) on to the master
* 

## The playbooks

First off, this assumes that you use Doug's [kube-centos-ansible](https://github.com/dougbtv/kube-centos-ansible) to spin up a cluster.

Once you've got the cluster running, move into the ansible dir here, `./k8s/ansible` and check out the inventory file, `./inventory/vms.inventory` and customize it to match your... well, your inventory.

Now, let's `preload` this, for now this will primarily download some goodies that you need (it downloads the asterisk docker images, which are biiiig).

    ansible-playbook -i inventory/vms.inventory preload.yml

Once you're preloaded, you can continue on to labelling.

This playbook essentially does:

```
[root@kube-master centos]# kubectl label nodes kube-minion-2 voiptype=tandem
node "kube-minion-2" labeled
[root@kube-master centos]# kubectl get nodes --show-labels | grep minion-2 | awk '{print $4}'
beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/hostname=kube-minion-2,voiptype=tandem
```

Giving the `kube-minion-2` a voiptype, as that's where we're going to run our asterisk pod. It's going to be our tandem switch.

    ansible-playbook -i inventory/vms.inventory labels.yml

Now we can go ahead and template the pod spec.

    ansible-playbook -i inventory/vms.inventory load_podspec.yml

From the master we can now start up that pod...

    kubectl create -f asterisk.yml

And you can see it be created...

    watch -n1 kubectl get pods

And now you can describe it

     kubectl describe pod asterisk

And you can run the asterisk CLI :D

     kubectl exec -it asterisk -- /usr/sbin/asterisk -r

