# Robinson Valid Drawings

Code used in the computational experiments of our work on valid drawings of Robinson spaces. The repository includes tools to find valid caterpillar drawings and compare different formulations of the associated linear programming models.

## Files

| File | Description |
|------|-------------|
| `caterpillar_metric.py` | Main script: builds and solves the LP to determine whether a Robinson space admits a valid drawing in a caterpillar. |
| `compare_restrictions.py` | Generates random Robinson spaces and compares the number of constraints in different LP formulations. |
| `create_Robinson.r` | Generates random Robinson matrices using the `seriation` package in R. |
| `utils.py` | Helper functions: center-matrix computations, solution verification, and caterpillar representation. |

## Requirements

- Python 3.x
- R
- `numpy`, `pandas`, `matplotlib`, `networkx`
- `pulp` (LP solver wrapper; uses CBC by default)
- R package `seriation`

Install Python dependencies:

```bash
pip install numpy pandas matplotlib networkx pulp
```

Install the R package:

```r
install.packages("seriation")
```

## Usage

### 1. Finding valid caterpillar drawings

```bash
python caterpillar_metric.py [options]
```

#### Options

| Flag | Description |
|------|-------------|
| `-e N` | Use built-in example number N. |
| `-f FILE` | Read input matrix from a CSV file. |
| `-g SIZE` | Generate a random Robinson matrix of the given size. |
| `-m SIZE` | Generate a random center matrix of the given size. |
| `-d` | Treat input as a **distance** matrix (default: similarity). |
| `-c` | Treat input as a **center** matrix. |
| `-p` | Restrict the resulting structure to a **path**. |
| `-v` | Verbose output: print additional solution information and draw the caterpillar. |

#### Examples

Run using a built-in example:

```bash
python caterpillar_metric.py -e 0
```

Read a CSV distance matrix:

```bash
python caterpillar_metric.py -f my_matrix.csv -d
```

Generate and test a random center matrix of size 6:

```bash
python caterpillar_metric.py -m 6
```

### 2. Comparing LP formulations

```bash
python compare_restrictions.py n_size n_iterations
```

Where:
- `n_size`: Size of the random Robinson matrices.
- `n_iterations`: Number of random instances to generate.

Example:

```bash
python compare_restrictions.py 10 100
```

This generates 100 random Robinson matrices of size 10 and compares the number of constraints required by the different formulations.

### 3. Generating random Robinson matrices

```bash
Rscript create_Robinson.r
```

The script generates a random Robinson matrix and saves it as `random_robinson_matrix.csv`.

## Output

- **`caterpillar_metric.py`**: Reports the LP status and whether a valid caterpillar drawing was found. It also produces the output distance matrix and intermediate matrices used in the formulation.
- **`compare_restrictions.py`**: Generates CSV files containing the constraint counts for each instance and summary statistics.
- **`create_Robinson.r`**: Generates a CSV file containing a random Robinson matrix.

## How it works

1. **Random instances**: Robinson matrices are generated using the `seriation` package in R.
2. **Caterpillar metric**: The main LP formulation is used to find a valid drawing of the input Robinson space in a caterpillar.
3. **Constraint comparison**: Random instances are used to compare the number of constraints in the different LP formulations.
4. **Verification**: Auxiliary functions check the resulting metric and its validity as a drawing of the input Robinson space.