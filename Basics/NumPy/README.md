# Some `numpy` functions:

## `numpy.random`

NumPy's `np.random` module contains a suite of functions that are used for generating random numbers and performing
random operations, which are essential for tasks such as simulations, testing, and data sampling. Below is an overview
of the **most commonly used functions** within the `np.random` module:

### 1. Random Sampling

- **`rand(d0, d1, ..., dn)`**:
  Generates values in a given shape.

```python
np.random.rand(2, 3)  # 2x3 matrix in [0,1)
```

- **`randn(d0, d1, ..., dn)`**:
  Returns a sample (or samples) from the "standard normal" distribution.

```python
np.random.randn(2, 3)  # 2x3 matrix from the standard normal distribution
```

- **`randint(low, high, size, dtype)`**:
  Return random integers from `low` (inclusive) to `high` (exclusive).

```python
np.random.randint(1, 10, size=(3, 3))  # 3x3 matrix with random integers from 1 to 9
```

- **`random([size])`**:
  Return random floats in the half-open interval [0.0, 1.0).

```python
np.random.random((2, 2))  # 2x2 matrix in [0,1)
```

- **`choice(a[, size, replace, p])`**:
  Generates a random sample from a given 1-D array.

```python
np.random.choice([1, 2, 3, 4, 5], size=3, replace=False)  # Sample 3 elements without replacement
```

### 2. Permutations

- **`shuffle(x)`**:
  Modifies a sequence in-place by shuffling its contents.

```python
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)  # shuffled array
```

- **`permutation(x)`**:
  Randomly permute a sequence, or return a permuted range.

```python
np.random.permutation(10)  # permutation of numbers from 0 to 9
```

### 3. Distributions

- **`normal(loc=0.0, scale=1.0, size=None)`**:
  Draw random samples from a normal (Gaussian) distribution.

```python
np.random.normal(0, 1, size=(2, 2))  # 2x2 matrix from a normal distribution with mean 0 and std 1
```

- **`uniform(low=0.0, high=1.0, size=None)`**:
  Draw samples from a uniform distribution.

```python
np.random.uniform(0, 1, size=4)  # 4 samples from a uniform distribution between 0 and 1
```

- **`binomial(n, p, size=None)`**:
  Draw samples from a binomial distribution.

```python
np.random.binomial(10, 0.5, size=10)  # 10 samples from a binomial distribution with n=10, p=0.5
```

- **`poisson(lam=1.0, size=None)`**:
  Draw samples from a Poisson distribution.

```python
np.random.poisson(5, size=10)  # 10 samples from a Poisson distribution with lambda=5
```

- **`exponential(scale=1.0, size=None)`**:
  Draw samples from an exponential distribution.

```python
np.random.exponential(1, size=4)  # 4 samples from an exponential distribution with scale=1
```

### 4. Random Generator and Seed

- **`seed([seed])`**:
  Seed the generator for reproducibility.

```python
np.random.seed(42)  # Seed the random number generator
```

- **`RandomState`**:
  Container for the Mersenne Twister pseudo-random number generator.

```python
rng = np.random.RandomState(42)
rng.rand(3, 3)  # Generate numbers using the seeded RNG
```

This overview covers the most commonly used functions in the `np.random` module, which are enough for a wide range of
applications involving random number generation in scientific computing with Python.

## Broadcasting

Broadcasting is a powerful concept used in many programming and mathematical environments, particularly in libraries like NumPy in Python, which is used for numerical computations. It describes how arrays with different shapes are treated during arithmetic operations. The goal of broadcasting is to make arrays with different shapes compatible for element-wise operations without necessarily copying data to match sizes.

### How Broadcasting Works

1. **Compatibility Check**: Broadcasting starts by ensuring that the arrays are compatible for the operation. Two dimensions are compatible when:
   - they are equal, or
   - one of them is 1

2. **Shape Adjustment**: If the arrays do not have the same rank, prepend the shape of the lower-rank array with ones until both shapes have the same length.

3. **Dimension Expansion**: For any dimension where one array had size 1 and the other did not, the array with size 1 is virtually replicated to match the size of the other array.

### Example in NumPy

Consider two arrays, `A` with shape (4, 1) and `B` with shape (1, 3). Here's how broadcasting enables their addition:

```python
import numpy as np

A = np.array([[1], [2], [3], [4]])  # Shape (4, 1)
B = np.array([[5, 6, 7]])          # Shape (1, 3)

# Broadcasting A and B to shape (4, 3)
C = A + B
print(C)
```

Output:
```
[[ 6  7  8]
 [ 7  8  9]
 [ 8  9 10]
 [ 9 10 11]]
```

### Benefits of Broadcasting

- **Memory Efficiency**: Broadcasting avoids the explicit replication of data, which can be a significant advantage in terms of memory usage, especially with large arrays.
- **Vectorization**: By using broadcasting, operations can be vectorized, which means they are formulated as array operations rather than loop operations. This can result in significant performance improvements.

### Use Cases

- **Data Normalization**: Applying a mean subtraction or scaling operation across an entire array.
- **Applying Functions**: Efficiently applying functions across different dimensions of an array without loops.
- **Meshgrid Operations**: Generating coordinate matrices from coordinate vectors.

Broadcasting is a cornerstone of efficient array operations and is widely used in data science, machine learning, and any field that requires extensive numerical computation. Understanding and using broadcasting can lead to more efficient and cleaner code.

<!--
## References
Read the Advanced Python from the CS108 Folder.
-->