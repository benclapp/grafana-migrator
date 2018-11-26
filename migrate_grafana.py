#!/usr/bin/env python3

import argparse
import datasources
from dashboards import *
import snapshots
import json
import time
import grafana

parser = argparse.ArgumentParser(description='Import and export various grafana objects. One import type is required.')

import_flags = parser.add_mutually_exclusive_group(required=True)
import_flags.add_argument('--all', action='store_true', dest='import_all', help='Migrate ALL data (datasources, folders, dashboards, snapshots)')
import_flags.add_argument('--ds', '--datasources', action='store_true', dest='import_ds', help='Migrate datasources')
import_flags.add_argument('--db', '--dashboards', action='store_true', dest='import_db', help='Migrate dashboards (and folders)')
import_flags.add_argument('--ss', '--snapshots', action='store_true', dest='import_ss', help='Migrate snapshots')

gconf = parser.add_argument_group('Grafana Configs')
gconf.add_argument('--source-server', type=str, dest='source_server', required=True,
                    help='The grafana server to migrate data FROM', )
gconf.add_argument('--source-apikey', type=str, dest='source_apikey', required=True,
                    help='The api key for the grafana instance to migrate data FROM')
gconf.add_argument('--target-server', type=str, dest='target_server', required=True,
                    help='The grafana server to migrate data TO')
gconf.add_argument('--target-apikey', type=str, dest='target_apikey', required=True,
                    help='The api key for the grafana instance to migrate data TO')

args = parser.parse_args()

source = dict(server = args.source_server, apikey = args.source_apikey)
target = dict(server = args.target_server, apikey = args.target_apikey)

if args.import_all:
    print('Migrating all data')
elif args.import_ds:
    print('Migrating datasources only')
elif args.import_db:
    print('Migrating dashboards (and folders) only')
elif args.import_ss:
    print('Migrate snapshots')

if args.import_ds or args.import_all:
    _datasources = datasources.get_list(source)
    for datasource in _datasources:
        datasources.create_new(target, datasource)


if args.import_db or args.import_all:
    results = get_search_results(source, '0')

    for result in results:
        if result.get('type') == "dash-folder":
            folder = result
            target_folder_id = create_folder(target, folder)

            dbs = get_search_results(source, folder.get('id'))
            for db in dbs:
                _db = get_db(source, db.get('uid'))
                create_db(target, _db, target_folder_id)

        elif result.get('type') == "dash-db":
            db = result
            _db = get_db(source, db.get('uid'))
            create_db(target, _db, 0)

if args.import_ss or args.import_all:
    _snapshots = snapshots.list(source)
    for snapshot in _snapshots:
        _snapshot = snapshots.get_ss(source, snapshot.get('key'))
        snapshots.create(target, _snapshot)
