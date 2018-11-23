#!/usr/bin/env python3
 
import requests
import json


def grafana_client(conn_details, path):
    """Returns result of Grafana query as json."""

    url = conn_details.get("server") + path
    headers = {'Authorization': str("Bearer " + conn_details.get("apikey"))}

    r = requests.get(url, headers=headers)

    r.raise_for_status()

    return r.json()