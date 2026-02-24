# Robinson_valid_drawing
Tools related to finding valid drawings for Robinson spaces using Python

## Requirements:
- R, with the "seriation" library installed
- PuLP library in Python installed

## How to use

To run this project, you must execute the script "compare_restrictions.py" as follows:

> python3 compare_restrictions.py n_size n_iterations

Where:

- n_size denotes the size of the Robinson spaces that will be tested.
- n_iterations denotes the amount of randomly generated Robinson spaces that will be tested.

The code will generate two files, "results_{n_size}.csv" that writes the amount of restrictions for each Robinson space tested, and "summary_{n_size}.csv", that writes the average and the standard deviation for both methods tested.

We show a line example to run this code.

> python3 compare_restrictions.py 10 100

Here, the code will generate 100 random Robinson matrices of size 10 using the generator from the "seriation" library in R, and will count the amount of restrictions for each formulation of the linear programs used, writing these results in the files "resuñts_10.csv" and "summary_10.csv". 


