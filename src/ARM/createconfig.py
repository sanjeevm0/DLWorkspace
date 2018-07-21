import argparse



Dashboards:
  grafana:
    servers: sanjeevmk8s7-infra01.northcentralus.cloudapp.azure.com
  influxDB:
    servers: sanjeevmk8s7-infra01.northcentralus.cloudapp.azure.com
DeployAuthentications:
- Corp
- Gmail
- Live
UserGroups:
  DLWSAdmins:
    Allowed:
    - jinl@microsoft.com
    - jinlmsft@hotmail.com
    - jinli.ccs@gmail.com
    - sanjeevm@microsoft.com
    gid: "20001"
    uid: "20000"
  DLWSRegister:
    Allowed:
    - '@gmail.com'
    gid: "20001"
    uid: 20001-29999
WebUIadminGroups:
- DLWSAdmins
WebUIauthorizedGroups:
- DLWSAdmins
WebUIregisterGroups:
- DLWSRegister
WinbindServers: []
azure_cluster:
  sanjeevmk8s7:
    azure_location: northcentralus
    worker_vm_size: Standard_D2
    last_scaled_node_num: 0
    worker_node_num: 1
cloud_config:
  dev_network:
    source_addresses_prefixes:
    - 73.109.29.0/24
    - 167.220.0.0/16
    - 131.107.0.0/16
    - 52.151.11.0/24
    - 52.226.68.0/24
cloud_influxdb_node: sanjeevmk8s7-infra01.northcentralus.cloudapp.azure.com
cluster_name: sanjeevmk8s7
datasource: MySQL
mysql_password: M$ft2017
webuiport: 3080
