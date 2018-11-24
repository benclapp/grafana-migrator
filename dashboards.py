#!/usr/bin/env python3
from grafana import *

def get_search_results(grafana, folderid):
    print("Getting search results for folder ID " + str(folderid))
    q_params = {'query':'', 'folderIds': str(folderid)}
    return get_with_params(grafana, "/api/search", q_params)

def get_db(grafana, uid):
    print("Gettind dashboard with uid " + uid)
    dash = get(grafana, str("/api/dashboards/uid/" + uid))
    return dash

def create_folder(grafana, src_folder):
    print("Creating folder " + src_folder.get('title'))
    post(grafana, "/api/folders", src_folder)

def create_db(grafana, db):
    print('Creating dashboard ' + db['dashboard']['title'] + ' ' + db['dashboard']['uid'])
    post(grafana, "/api/dashboards/db", db)