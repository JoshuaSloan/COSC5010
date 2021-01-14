'''
Please note that I obtained help for this implementation from
https://github.com/javiajinkal/Flajolet-Martin
'''

# import libraries
import mmh3
import statistics
import math

# define function to determine the number of trailing 0's
def trailing_zeros(n):
	s = str(n)
	return len(s)-len(s.rstrip('0'))

# declare the data stream as list of input files
input_file =   ['quotes_2008-08.txt','quotes_2008-09.txt','quotes_2008-10.txt','quotes_2008-11.txt','quotes_2008-12.txt',
		'quotes_2009-01.txt','quotes_2009-02.txt','quotes_2009-03.txt','quotes_2009-04.txt']

# define the number of hashes
#numHashes = 4
numHashes = 6

# intialize result storage
result = [ "" for i in range(numHashes)]
result_tail = [[] for i in range(numHashes)]

# Flajolet-Martin Algorithm implementation	
for i in input_file:
    print("Working through",i,"...")
    fp = open(i,"r", encoding='ISO-8859-1')
    for line in fp:
        stream = line.split("\t")
        if stream[0] is 'Q':
            for seed in range(numHashes):
                result[seed] = format(abs(mmh3.hash(stream[1], seed)), '032b')
                result_tail[seed].append(trailing_zeros(result[seed]))
    fp.close()

# calculate and print estimation results   
group1 = 0
group2 = 0

for i in range(int(numHashes/2)):
    group1 = group1 + (2**(max(result_tail[i])))
group1 = group1/float(numHashes/2)

for i in range(int(numHashes/2)):
    group2 = group2 + (2**(max(result_tail[int(numHashes/2)+i])))
group2 = group2/float(numHashes/2)

print ("Estimated number of distinct quotes:",math.ceil(statistics.median([group1, group2])))