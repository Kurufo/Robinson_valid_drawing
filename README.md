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

We show a line example to run this code.

> python3 compare_restrictions.py 10 100

Here, the code will generate 100 random Robinson matrices of size 10 using the generator from the "seriation" library in R, and will try to find a valid drawing in a caterpillar for each of them using the PuLP library.


