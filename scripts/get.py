#!/usr/bin/env python

# Copyright (c)2016 Digium, Inc.
# Source: http://blogs.asterisk.org/2016/03/09/pushing-pjsip-configuration-with-ari/
# Written by: Mark Michelson

import requests
import json

url = "http://localhost:8088/ari/asterisk/config/dynamic/res_pjsip/auth/alice"

resp = requests.get(url, auth=('asterisk', 'asterisk'))

if resp.status_code == 200:
    print "Received object"
    print json.dumps(resp.json(), sort_keys=True, indent=2,
                     separators=(',', ': '))
else:
    print "Received {0} response".format(resp.status_code)
