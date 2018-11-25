# Grafana Migratior

Some scripts to assist with the migration of Grafana storage from sqlite3 to postgreSQL. Although could really be used from any Grafana instance to another, where database migration is not possible.

Will migrate the following:
- Datasources
- Dashboards (and folders)
- Snapshots

This will need to be run for each Organisation, as the API keys used here are scoped per organisation. 

## Usage

```bash
./migrate_grafana.py -h

./migrate_grafana.py --all --source-server $sourceServer --source-apikey $sourceKey --target-server $targetServer --target-apikey $targetKey 
```
