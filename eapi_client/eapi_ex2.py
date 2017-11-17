import pyeapi
from pprint import pprint as pp

host1 = pyeapi.connect_to("sw1")
host2 = pyeapi.connect_to("sw2")

devices = [host1, host2]

value = 0

for host in devices:
    value += 1
    print(str(value))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Pre-change State: ", host)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    pp(host.enable(['show hostname', 'show running-config']))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Post-Change State:", host)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    host.config(['interface loopback 0', 'ip address 1.1.1.{} 255.255.255.255'.format(value), 'description test'])
    pp(host.enable('show running-config'))
    

