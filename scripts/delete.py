#!/usr/bin/env python

# Copyright (c)2016 Digium, Inc.
# Source: http://blogs.asterisk.org/2016/03/09/pushing-pjsip-configuration-with-ari/
# Written by: Mark Michelson

import requests

url = 'http://localhost:8088/ari/asterisk/config/dynamic/res_pjsip/auth/alice'

resp = requests.delete(url, auth=('asterisk', 'asterisk'))

if resp.status_code == 204:
    print "Successfully deleted"
else:
    print "Received {0} response".format(resp.status_code)
