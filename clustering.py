import pandas as pd
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage

data = pd.read_csv('/Users/jrobertson/Desktop/Heidelberg_snp_mat.txt',sep='\t',header=0,index_col=0)
data_labels = data.columns.values
distance_matrix = data.as_matrix()


condensed_matrix = scipy.spatial.distance.squareform(distance_matrix)

Z = scipy.cluster.hierarchy.linkage(condensed_matrix, method='single')

dists = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100)

clust_assignments = dict()

for dist in dists:
    index = 0
    clusters = fcluster(Z, dist, criterion='distance')
    for id in data.columns.values:
        if not id in clust_assignments:
            clust_assignments[id] = list()
        clust_assignments[id].append(str(clusters[index]))
        index += 1

for id in clust_assignments:
    print ("{}\t{}".format(id,"\t".join(clust_assignments[id])))




