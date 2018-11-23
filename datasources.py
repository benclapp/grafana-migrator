#!/usr/bin/env python3
from grafana import grafana_get
from grafana import grafana_post

def get_list(grafana):
    """Returns a list of datasources"""
    print("Getting list of data sources...")

    datasources = grafana_get(grafana, "/api/datasources")
    return datasources

def sanitize(datasource):
    """Removes some IDs so we can create a new datasource"""
    print("  - Sanitizing datasources for population")

    datasource.pop('id')
    datasource.pop('orgId')
    return datasource

def create_new(grafana, datasource):
    """Creates a new datasource against the target grafana"""
    print("  - Creating datasource")

    grafana_post(grafana, '/api/datasources', datasource)
