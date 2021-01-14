To view the output from running the Jupyter Notebook file, view the data_mining_hw5_q5.html file.*
*For indiviudal answers, view the top 5 words plus counts for 10 clusters and top 500 words plus counts text files.

In order to run the data_mining_hw5_q4.ipynb file, you need to have Anaconda installed (as well as Jupyter Notebook).

From there, simply open the file in Jupyter Notebook and click "restart the kernel, then re-run the whole notebook (with dialog)"
This took approximately 1 minute and 52 seconds to run all the way through on my machine, so be patient!

Alternatively, you can run cells indiviudally* 
(*NOTE: they must be ran in sequential order, as previous cells depend on variables previously defined in earlier cells)

The following packages are required:
numpy
pandas
string
sklearn

Any base Python 3.7 environment should automatically come installed with all of the necessary import packages*.
*For a more detailed list of base packages, plese see: https://docs.anaconda.com/anaconda/packages/pkg-docs/

Should any imports be missing (there should not be any) simply use:

conda install "package name"

in the terminal/command prompt.

Depending on how the k-means clustering assigns data vectors, your results might differ slightly. However, overall results should generally look the same.

It is important to note than in my implementation, I removed all punctuation, HTML tags and cast all strings to lowercase prior to clustering (string representations of numbers remain).
