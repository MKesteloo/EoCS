import csv
import socket
import numpy as np


# Compute distance between IP addresses
def distance(ip1, ip2):
    if len(ip1) != len(ip2):
        return
    return abs(ip1[0]-ip2[0]) + abs(ip1[1]-ip2[1]) +abs(ip1[2]-ip2[2]) + abs(ip1[3]-ip2[3])


# Convert list of int into an IP string representation
def find_ip(ip):
    return '.'.join([str(x) for x in ip])


# --------------------- MAIN -----------------------------------


data_headers = []
data = []
ips = []

with open('processed_data.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=",",skipinitialspace=True)
    data_headers = reader.fieldnames

    for row in reader:
        data.append(row)
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
# import plotly.plotly as py
# import plotly.figure_factory as ff
# from plotly.offline import offline
# fig = ff.create_dendrogram(np.array(ips))
# offline.plot(fig, filename='file.html')


# Clustering
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import fcluster

Z = linkage(ips, 'average')#, metric=distance)
c, coph_dists = cophenet(Z, pdist(ips))
# 'Z' holds data: [idx1, idx2, dist, sample_count]
print Z
print c
print len(Z)

# calculate dendrogram
from matplotlib import pyplot as plt
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

# This does not work yet. Extracting raw samples from each cluster
# https://stackoverflow.com/questions/15951711/how-to-compute-cluster-assignments-from-linkage-distance-matrices-in-scipy-in-py
cluster = fcluster(Z, 20)
