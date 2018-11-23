#!/usr/bin/env python3
 
import requests
import json

def grafana_get(conn_details, path):
    """Returns result of Grafana query as json."""

    url = str(conn_details.get("server")) + str(path)
    headers = {'Authorization': str("Bearer " + conn_details.get("apikey"))}
    r = requests.get(url, headers=headers)

    r.raise_for_status()

    return r.json()

def grafana_post(conn_details, path, body):
    """Posts a request"""

    url = conn_details.get("server") + path
    headers = {'Authorization': str("Bearer " + conn_details.get("apikey"))}

    r = requests.post(url, headers=headers, data=body)
    r.raise_for_status
    
