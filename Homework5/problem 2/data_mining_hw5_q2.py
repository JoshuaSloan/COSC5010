# import libraries
from bloomfilter import BloomFilter 
from random import shuffle
import math

# open the usernames file for S
file = open("listed_username_30.txt",encoding="utf8")

# read in the data to S
Lines = file.readlines() 
S = [] 
for line in Lines: 
    S.append(line)

# open the usernames file for our data stream
file2 = open("listed_username_365.txt",encoding="utf8")

# read in the stream data
Lines2 = file2.readlines() 
S2 = []
for line in Lines2: 
    S2.append(line)

#number of items to add 
n = len(S) 

# print the size of n
print("Size of S:",n)

# create bloom filter
bloomf = BloomFilter(n)
print("Size of bit array:{}".format(bloomf.size)) 
print("Number of hash functions:{}".format(bloomf.hash_count)) 

FPR = (1-math.exp((-bloomf.hash_count*n)/bloomf.size))**bloomf.hash_count
print("Computed False Positive Probability:",FPR)

# add all elements in S to filter
for item in S: 
    bloomf.add(item) 

# test the filter's FPR on multiple subsets of the stream
print("\nVerifying False Positive Probability on random subsets of the stream data...")
for i in range(10):
    shuffle(S2)
      
    test_words = S2[:10000]
    shuffle(test_words) 
    
    FP = 0
    total = 0
    for word in test_words: 
        if bloomf.check(word): 
            if word in S: 
                #FP = FP+1
                total = total+1
            else: 
                FP = FP+1
                total = total+1
        else: 
            total = total+1
    
    print("Subset",i+1,":",FP/total)