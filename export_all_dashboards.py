"""Will download grafana dashboards for you"""
from urllib.request import Request, urlopen
import json

GRAFANA_API_URL = "http://macserver:3000/api/"
GRAFANA_SEARCH_PATH = "search/"
GRAFANA_API_KEY = "eyJrIjoiSGVzNjV0aXYyemt4NDVZbUsyaWZtaDJ2aXBRV3IwTmEiLCJuIjoiQmVuIiwiaWQiOjF9"

print("GRAFANA_API_URL: ", GRAFANA_API_URL)

#urlopen(GRAFANA_API_URL + "api/search/").read()

def log(msg):
    print(msg)

def query_grafana(path):
    """Returns result of Grafana query as json data. \n
    Provide path please."""
    uri = GRAFANA_API_URL + path
    print(f"Request Uri: {uri}")
    req = Request(uri)
    req.add_header('Authorization', f'Bearer {GRAFANA_API_KEY}')
    resp = urlopen(req)
    return json.loads(resp.read().decode())

def get_dashboard_list():
    """returns dictionary of dashboards"""
    search_result = query_grafana(GRAFANA_SEARCH_PATH)
    db_count = len(search_result)
    log(f"{str(db_count)}(s) to export.")
    return search_result

def list_dashboards(search_result):
    """gets all the dashboards"""
    log("Listing Dashboards")
    for db in search_result:
        title = db["title"]
        uri = db["uri"]
        log(f"exporting: {title} to {title}.json")
        dash = query_grafana(f"dashboards/{uri}")
        with open(f"{title}.json", "w") as json_file:
            json.dump(dash, json_file, indent=4)


#get_dashboard_list()
list_dashboards(get_dashboard_list())
