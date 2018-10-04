import csv
import socket
import numpy as np


def distance(ip1, ip2):
    if len(ip1) != len(ip2):
        return
    return abs(ip1[0]-ip2[0]) + abs(ip1[1]-ip2[1]) +abs(ip1[2]-ip2[2]) + abs(ip1[3]-ip2[3])


data_headers = []
ips = []

with open('processed_data.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=",",skipinitialspace=True)
    data_headers = reader.fieldnames

    for row in reader:
        ip = row.get(data_headers[7]).split(".")
        ips.append([int(x) for x in ip])

# unique only
ips = [list(x) for x in set(tuple(x) for x in ips)]

# for ip1 in ips:
#     for ip2 in ips:
#         if ip1 == ip2:
#             continue
#         print ip1, ip2, distance(ip1, ip2)


# Create dendrogram to determine optimal number of clusters
import plotly.plotly as py
import plotly.figure_factory as ff
from plotly.offline import offline

fig = ff.create_dendrogram(np.array(ips))
offline.plot(fig, filename='file.html')