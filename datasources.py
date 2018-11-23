#!/usr/bin/env python3
from grafana import grafana_client

def get_list(source):
    datasources = grafana_client(source, "/api/datasources")
    return datasources

def create_new(server)