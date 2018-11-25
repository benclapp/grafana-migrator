#!/usr/bin/env python3
from grafana import *

def list(grafana_instance):
    print("Getting list of snapshots...")

    snapshots = get(grafana_instance, "/api/dashboard/snapshots")
    return snapshots

def get_ss(grafana_instance, key):
    print("Getting snapshot with key " + key)

    snapshot = get(grafana_instance, "/api/snapshots/" + str(key))
    return snapshot

def create(grafana_instance, snapshot):
    title = snapshot['dashboard']['title']
    print("Creating snapshot " + str(title))

    snapshot.pop('meta')
    snapshot['name'] = title

    post_json_contenttype(grafana_instance, "/api/snapshots", snapshot)
