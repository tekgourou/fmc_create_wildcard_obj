from fmcapi import *
import time

# Set these variables to match your environment. ### #
host = 'YOUR FMC IP or HOSTNAME'
username = 'FMC USERNAME WITH ADMIN or API ROLE'
password = 'FMC PASSWORD'

# Set name and value
autodeploy = False
wildcard_count = 256
group_name = 'WILDCARD OBJECT GROUP NAME'
subnet_object_name_prefix = 'subnet_wildcard'
subnet_object_value_wildcard = '10.56.x.0/26'

# Script
def add_network_to_a_group(subnet_object_name,subnet_object_value, group_name ):
    obj10 = Networks(fmc=fmc1, name=subnet_object_name, value=subnet_object_value)
    obj10.post()
    time.sleep(1)
    obj1 = NetworkGroups(fmc=fmc1, name=group_name)
    obj1.get()
    obj1.named_networks(action='add', name=obj10.name)
    obj1.post()

with FMC(host=host, username=username, password=password, autodeploy=autodeploy) as fmc1:
    for x in range(wildcard_count):
        subnet_object_name = '{}_{}'.format(subnet_object_name_prefix,x)
        subnet_object_value = subnet_object_value_wildcard.replace('x', str(x))
        add_network_to_a_group(subnet_object_name, subnet_object_value, group_name)

