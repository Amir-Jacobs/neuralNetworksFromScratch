import numpy as np

# each neuron has inputs, weights and a bias
inputs = [2, 4.5, 1, 7]

weights = [
    [0.5, 1.0, 0.3, 0.9],
    [0.1, 0.9, 0.4, 0.2],
    [0.6, 0.2, 0.1, 0.8]
]

biases = [2, 1, 4]

# the output sums each input with its corresponding weight, and then adds the bias
output = np.dot(weights, inputs) + biases

# show result
print(output)