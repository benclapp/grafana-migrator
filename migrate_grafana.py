#!/usr/bin/env python3
# eyJrIjoiT0FTdXVwV2xzUW5MYkwzNm5iYzJMMTU1ckttN1NZbEQiLCJuIjoiRGF0YUV4cG9ydGVyIiwiaWQiOjF9

import argparse
import datasources
import dashboards

parser = argparse.ArgumentParser(description='Import and export various grafana objects.')
parser.add_argument('--source-server', type=str, dest='source_server', required=True,
                    help='The grafana server to migrate data FROM')
parser.add_argument('--source-apikey', type=str, dest='source_apikey', required=True,
                    help='The api key for the grafana instance to migrate data FROM')
parser.add_argument('--target-server', type=str, dest='target_server', required=True,
                    help='The grafana server to migrate data TO')
parser.add_argument('--target-apikey', type=str, dest='target_apikey', required=True,
                    help='The api key for the grafana instance to migrate data TO')

args = parser.parse_args()

source = dict(server = args.source_server, apikey = args.source_apikey)
target = dict(server = args.target_server, apikey = args.target_apikey)



search_result = grafana.grafana_client(args.server, args.apikey, "api/search/")
print(json.dumps(search_result, indent=4, sort_keys=True))


datasources = datasources.get_list(source)
for datasource in datasources
    create_new_source(datasource)


dashboards = get_dashboards()
for dashboard in dashboards
    db = get_dashboard(dashboard)
    db = sanitize_dashboard(db)
    create_new_dashboard(db)
