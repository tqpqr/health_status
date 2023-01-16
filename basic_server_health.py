#!/usr/bin/env python3

import shutil
import psutil
import os
import requests


cpu = psutil.cpu_percent()
hdd = psutil.disk_usage('/').percent
memory = psutil.virtual_memory()
#network = psutil.net_connections()
#network2 = psutil.net_if_addrs()
network3 = psutil.net_io_counters()
print(cpu)
print(hdd)
print(memory[2])
print(network3)
#print(network2)
