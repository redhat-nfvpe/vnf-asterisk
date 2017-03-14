# vnf-asterisk under Kubernetes

Here's a series of instructions of how to get vnf-asterisk running under k8s.

## The playbooks

First off, this assumes that you use Doug's [kube-centos-ansible](https://github.com/dougbtv/kube-centos-ansible) to spin up a cluster.

Once you've got the cluster running, move into the ansible dir here, `./k8s/ansible` and check out the inventory file, `./inventory/vms.inventory` and customize it to match your... well, your inventory.

Now, let's bootstrap this, for now this will primarily download some goodies that you need.

