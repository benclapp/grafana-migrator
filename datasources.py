#!/usr/bin/env python3
from grafana import get
from grafana import post

def get_list(grafana):
    """Returns a list of datasources"""
    print("Getting list of data sources...")

    datasources = get(grafana, "/api/datasources")
    return datasources

def create_new(grafana, datasource):
    """Creates a new datasource against the target grafana"""

    print("Creating datasource " + datasource.get('name'))
    datasource.pop('id')
    datasource.pop('orgId')

    post(grafana, '/api/datasources', datasource)

