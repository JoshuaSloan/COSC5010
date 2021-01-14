# import all necessary libraries
import time
import warnings
import numpy as np
import networkx as nx
from sklearn.cluster import SpectralClustering
from sklearn.metrics import confusion_matrix
from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score

# used to ignore deprication warning for affinity selection in spectral clustering
warnings.filterwarnings("ignore")

# read in the graph data
G = nx.read_gml('karate.gml', label = 'id')

# print graph information
print (nx.info(G),"\n")

# create ground truth array (i.e. student membership labels)
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,
0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]

# create adjacency matrix
adjMat = nx.adjacency_matrix(G)

# create algorithm run-time list
runTimes = []

for i in range(10):
    print("Trial",i+1)
    # start timer
    tic = time.perf_counter()
    
    # create and fit spectral clustering
    spectral = SpectralClustering(n_clusters=2, affinity="nearest_neighbors")
    spectral.fit(adjMat)
    
    # get spectral clustering label results and store them in a list
    results = list(spectral.labels_)
    
    # stop timer
    toc = time.perf_counter()
    
    # add trial run-time to list
    runTimes.append(f"{toc-tic:0.4f}")
    
    # print confusion matrix results
    TN, FP, FN, TP = confusion_matrix(groundTruth, results).ravel()
    print("True Positives:",TP)
    print("True Negatives:",TN)
    print("False Positives:",FP)
    print("False Negatives:",FN)
    
    # print NMI and Adjusted Rand Score
    print("Normalized Mutual Information Score:",normalized_mutual_info_score(groundTruth, results))
    print("Adjusted Rand Score:",adjusted_rand_score(groundTruth, results),"\n")

# get average algorithm run-time from list and print results
avRunTime = list(np.float_(runTimes))

print("The average run-time of this algorithm is",np.mean(avRunTime),"seconds.")