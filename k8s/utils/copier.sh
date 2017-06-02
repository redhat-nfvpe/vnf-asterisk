#!/bin/bash

# This is Doug's utility to copy the helm charts to where they need to be on a remote host.
rsync -az -e 'ssh -p 2222 -i ~/.ssh/id_testvms' ./vnf-asterisk-helm/* centos@localhost:/home/centos/vnf-asterisk-helm

