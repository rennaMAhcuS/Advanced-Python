# Matplotlib

## `np.meshgrid` for 3D Plots in Matplotlib

`np.meshgrid` is a function provided by NumPy, a fundamental package for scientific computing in Python. It is used to create a rectangular grid out of two given one-dimensional arrays representing the Cartesian indexing or Matrix indexing. `np.meshgrid` is particularly useful in 3D plotting, data analysis, and graphical visualization where operations are performed on a grid or mesh of points.

### How `np.meshgrid` Works:
- **Input**: Two or more one-dimensional arrays. Each array represents a dimension.
- **Output**: N 2D arrays (where N is the number of input arrays), with each 2D array representing a matrix where the rows are copies of the corresponding input array. If two input arrays are provided, the first output array varies along the rows, and the second varies along the columns.

### Usage:
- **3D Plotting**: In 3D plotting, `np.meshgrid` is used to create a grid of (x, y) coordinates for the domain of a function in two variables.
- **Vectorized Evaluations**: It allows for vectorized evaluations of functions over a grid, enabling efficient computations and simplifications in many numerical and scientific computing applications.

### Example:
To understand how `np.meshgrid` works, consider two arrays `x = [1, 2, 3]` and `y = [4, 5]`. Using `np.meshgrid(x, y)`, we get two 2D arrays. The first array contains copies of the `x` array repeated for each value in `y`, and the second array contains copies of the `y` array repeated for each value in `x`.

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5])

X, Y = np.meshgrid(x, y)

print("X:")
print(X)
print("Y:")
print(Y)
```

This code will output:

```
X:
[[1 2 3]
 [1 2 3]]
Y:
[[4 4 4]
 [5 5 5]]
```

Here, `X` represents the grid of `x` coordinates, and `Y` represents the grid of `y` coordinates. Together, they form a grid of points over which you can evaluate a function of two variables.

To use `np.meshgrid` for creating 3D plots in Matplotlib, you typically follow these steps:

1. **Import necessary libraries**: Import NumPy for numerical operations and Matplotlib for plotting.
2. **Generate grid data**: Use `np.meshgrid` with two 1D arrays to create a grid. This grid will be used for the X and Y coordinates.
3. **Define a function for Z**: Based on X and Y, define a function to calculate Z values. This function represents the surface or mesh you want to plot.
4. **Create a 3D plot**: Plot the surface using the X, Y, and Z data.

Here's an example code snippet that demonstrates these steps:

```python
import numpy as np
import matplotlib.pyplot as plt

ax_sur = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

ax_sur.plot_surface(X, Y, Z, cmap="Spectral")
ax_sur.set_title("3D Plot")

plt.show()
```

This code creates a 3D surface plot where the Z values are determined by the sine of the distance from the origin, producing a wavy pattern.