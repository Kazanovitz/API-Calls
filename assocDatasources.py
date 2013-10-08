#!/usr/bin/env

#
# basic_api_call.py
# Purpose:
#   Add abstraction and simplify the building of URL's,
#   making HTTPS requests (specifically RPC calls to LogicMonitor's API)
#
# Parameters:
#   Authentication - 
#      (String) c = companyname
#      (String) u = username
#      (String) p = password
#   (String) call -
#      The RPC to invoke
#   (Dictionary) params -
#      A dictionary of the parameters to be used in the API call
#      e.g {"property1": "value1", "integerProperty": 12345}
#
#
# Author: Ethan Culler-Mayeno
#

import urllib
import urlparse
import sys
import json
import os

COMPANY = "example"
USERNAME = "username"
PASSWORD = "pword"

def rpc(action, params):
    """Make a call to the LogicMonitor RPC library and return the response"""
    print "Calling action: %s" % action
    print "Parameters: %s" % str(params)
    param_str = urllib.urlencode(params)
    creds = urllib.urlencode({"c": COMPANY, "u": USERNAME, "p": PASSWORD})
    if param_str:
        param_str = param_str + "&"
    param_str = param_str + creds
    try:
        
        f = urllib.urlopen("https://{0}.logicmonitor.com/santaba/rpc/{1}?{2}".format(COMPANY, action, param_str))
        return f.read()

    except IOError as ioe:
        print ioe
    #end try
#end rpc


# print rpc("addAccount", {"username": "sublimeJono", "password": "jonathan", "roles": 4, "status": "active", "contactMethod":"email", "email": "subilme@winning.com", "viewPermission": "{Dashboards:true,Hosts:true,Services:true,Alerts:true,Reports:true,Settings:true}"})

#Author Jonathan Kassan

def assocDatasources(hostId, hostGroupId):
    response = rpc("getHostDataSourceGroups", {"hostId":hostId, "hostGroupId": hostGroupId, "withGraph": "false", "withDsi": "true"})
    decoded = json.loads(response)
    num = len(decoded[u'data'])
    numData = num   
    for i in range (0, numData):
        if (type (decoded[u'data'][i]) == dict and (decoded[u'data'][i]).has_key("items") ):  # checking if it's a group of datasources
            groupLen = len(decoded[u'data'][i][u'items'])
            Len = groupLen 
            for k in range (0, Len): # looping through group of datasources
                print decoded[u'data'][i][u'items'][k]['name'] # need to use 'name' because events don't have displayedAs
            #end for k
        #end if    
        else:
            print decoded[u'data'][i][u'group']['name'] 

    #end for i

#end







