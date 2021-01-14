This code was written in a Python 3.6 environment.

The only non-standard libraries utilized is the mmh3 (murmur hash) library and the bitarray library, which can be installed using:

"pip install mmh3"
and
"pip install bitarray"

in the terminal/command prompt respectively.

To run this code locally, please ensure that the corresponding data files are located in the same directory as the 2 python scripts(data_mining_hw5_q2.py and bloomfilter.py).

For this assignment, I obtained help from the following resource:
https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/

*NOTE: Verification results may be slightly lower than the predicted FPR, depending on how the shuffle function derived the testing subset! Overall, all trials were VERY close to the estimated FPR, leading me to believe that the implementation is correct.*