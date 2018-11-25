#!/usr/bin/env python3
from grafana import *

def get_search_results(grafana, folderid):
    print("Getting search results for folder ID " + str(folderid))
    q_params = {'query':'', 'folderIds': str(folderid)}
    return get_with_params(grafana, "/api/search", q_params)

def get_db(grafana, uid):
    dash = get(grafana, str("/api/dashboards/uid/" + uid))
    return dash

def create_folder(grafana, src_folder):
    print("Creating folder " + src_folder.get('title'))

    response = post(grafana, "/api/folders", src_folder)
    response_json = json.loads(response)

    return response_json.get('id')

def create_db(grafana, db, folderId):
    print('Creating dashboard ' + db['dashboard']['title'] + ' in folder ' + str(folderId))
    db.pop('meta')
    _db = db
    _db['dashboard']['id'] = None
    _db['overwrite'] = True
    _db['folderId'] = folderId
    _db['inputs'] = []

    post_json_contenttype(grafana, "/api/dashboards/import", _db)
