#!/usr/bin/env python3
# eyJrIjoiT0FTdXVwV2xzUW5MYkwzNm5iYzJMMTU1ckttN1NZbEQiLCJuIjoiRGF0YUV4cG9ydGVyIiwiaWQiOjF9

import argparse
import datasources
from dashboards import *
import json
import time
import grafana

parser = argparse.ArgumentParser(description='Import and export various grafana objects.')

import_flags = parser.add_mutually_exclusive_group(required=True)
import_flags.add_argument('--all', action='store_true', dest='import_all', help='Migrate ALL data (datasources, folders, dashboards)')
import_flags.add_argument('--ds', '--datasources', action='store_true', dest='import_ds', help='Migrate datasources')
import_flags.add_argument('--db', '--dashboards', action='store_true', dest='import_db', help='Migrate dashboards (and folders)')

gconf = parser.add_argument_group('Grafana Configs')
gconf.add_argument('--source-server', type=str, dest='source_server', required=True,
                    help='The grafana server to migrate data FROM', )
gconf.add_argument('--source-apikey', type=str, dest='source_apikey', required=True,
                    help='The api key for the grafana instance to migrate data FROM')
gconf.add_argument('--target-server', type=str, dest='target_server', required=True,
                    help='The grafana server to migrate data TO')
gconf.add_argument('--target-apikey', type=str, dest='target_apikey', required=True,
                    help='The api key for the grafana instance to migrate data TO')

def dump_json(dump_me):
    with open("dump.json", 'w') as outfile:
        json.dump(dump_me, outfile, indent=4, sort_keys=True)

args = parser.parse_args()

source = dict(server = args.source_server, apikey = args.source_apikey)
target = dict(server = args.target_server, apikey = args.target_apikey)

if args.import_all:
    print('Migrating all data')
elif args.import_ds:
    print('Migrating datasources only')
elif args.import_db:
    print('Migrating dashboards (and folders) only')

if args.import_ds or args.import_all:
    _datasources = datasources.get_list(source)
    for datasource in _datasources:
        datasources.create_new(target, datasource)


if args.import_db or args.import_all:
    results = get_search_results(source, '0')

    for result in results:
        if result.get('type') == "dash-folder":
            folder = result
            create_folder(target, folder)

            dbs = get_search_results(source, folder.get('id'))
            for db in dbs:
                _db = get_db(source, db.get('uid'))
                create_db(target, _db)

        elif result.get('type') == "dash-db":
            db = result
            _db = get_db(source, db.get('uid'))
            create_db(target, _db)
