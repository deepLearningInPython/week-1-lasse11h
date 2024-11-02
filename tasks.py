import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
def step(x):
    """Return 1 if x is greater than 0, otherwise return -1."""
    return 1 if x > 0 else -1


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu

# Your code here:
import numpy as np

def ReLu(arr, cutoff=0):
    # Ensure the input is a numpy array
    arr = np.array(arr)
    # Apply the ReLU transformation
    arr[arr < cutoff] = cutoff
    return arr
# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
def neural_net_layer(matrix, vector):
    # Ensure the vector is reshaped properly for matrix multiplication
    vector = vector.reshape(-1, 1)  # Reshape to (p, 1) if needed
    
    # Perform matrix multiplication
    result = np.dot(matrix, vector)
    
    # Apply the ReLU function to the result
    result = ReLu(result)
    
    return result
