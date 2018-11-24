#!/usr/bin/env python3
 
import requests
import json

def get(conn_details, path):
    """Returns result of Grafana query as json."""

    url = str(conn_details.get("server")) + str(path)
    headers = {'Authorization': str("Bearer " + conn_details.get("apikey"))}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def get_with_params(conn_details, path,  q_params):
    """Grafana request with query params"""
    
    url = str(conn_details.get("server")) + str(path) 
    headers = {'Authorization': str("Bearer " + conn_details.get("apikey"))}
    r = requests.get(url, headers=headers, params=q_params)
    r.raise_for_status()
    return r.json()

def post(conn_details, path, body):
    """Posts a request"""

    url = conn_details.get("server") + path
    headers = {
        'Authorization': str("Bearer " + conn_details.get("apikey"))
        }

    r = requests.post(url, headers=headers, data=body)
    # print(r.text)
    r.raise_for_status()
    
