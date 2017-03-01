#!/usr/bin/env python

# Copyright (c)2016 Digium, Inc.
# Copyright (c)2017 Red Hat, Inc.
# Source: http://blogs.asterisk.org/2016/03/09/pushing-pjsip-configuration-with-ari/
# Original source Written by: Mark Michelson
#
# Additional development by Leif Madsen

import requests
import json
import sys

def resp_check(resp):
    """Return status code of a response from sorcery"""
    if resp.status_code == 200:
        print "Successfully pushed"
        print json.dumps(resp.json(), sort_keys=True, indent=2,
                 separators=(',', ': '))
    else:
        print "Received {0} response".format(resp.status_code)

def resp_push(url, config):
    resp = requests.put(url, auth=('asterisk', 'asterisk'), json=config)
    return resp


# base URL to connect to Asterisk ARI interface for dynamic configuration
url = "http://localhost:8088/ari/asterisk/config/dynamic/res_pjsip/"

# Add pjsip sections / users / endpoints / auths etc
sections = {}
sections['alice'] = { 'username': 'alice', 'password': 'supersecret' }
sections['bob'] = { 'username': 'bob', 'password': 'supersecret' }

# Add Transports
#  -- for now don't do this dynamically as it results in a crash.
#     see https://issues.asterisk.org/jira/browse/ASTERISK-26829
#transport_url = url + "transport/transport-udp"
#
#transport_config = {
#    'fields': [
#        { 'attribute': 'protocol', 'value': 'udp' },
#        { 'attribute': 'bind', 'value': '0.0.0.0' },
#    ]
#}
#
#transport_resp = resp_push(transport_url, transport_config)
#resp_check(transport_resp)

# Add Auths
#  -- for SIPp scenarios, we're going to authenticate via identities
#     which allows for IP based authentication.
#auth_url = url + "auth/"
#
#for k, v in sections.iteritems():
#    auth_config = {
#        'fields': [
#            { 'attribute': 'username', 'value': v['username'] },
#            { 'attribute': 'password', 'value': v['password'] },
#        ]
#    }
#
#    auth_resp = resp_push(auth_url + k, auth_config)
#    resp_check(auth_resp)

# Add Endpoints
endpoint_url = url + "endpoint/"
for k, v in sections.iteritems():
    endpoint_config = {
        'fields': [
            { 'attribute': 'transport', 'value': 'transport-udp' },
            { 'attribute': 'context', 'value': 'endpoints' },
            { 'attribute': 'disallow', 'value': 'all' },
            { 'attribute': 'allow', 'value': 'ulaw' },
        ]
    }

    endpoint_resp = resp_push(endpoint_url + k, endpoint_config)
    resp_check(endpoint_resp)

# Add Identities
identity_url = url + "identify/"

for k, v in sections.iteritems():
    identifies_config = {
        'fields': [
            { 'attribute': 'endpoint', 'value': k },
            { 'attribute': 'match', 'value': '127.0.0.2' },
        ]
    }

    identity_resp = resp_push(identity_url + k, identifies_config)
    resp_check(identity_resp)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
