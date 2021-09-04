# each neuron has inputs, weights and a bias
inputs = [2, 4.5, 1, 7]

weights1 = [0.5, 1.0, 0.3, 0.9]
weights2 = [0,1, 0.9, 0.4, 0.2]
weights3 = [0.6, 0.2, 0.1, 0.8]

bias1 = 2
bias2 = 1
bias3 = 4

# the output sums each input with its corresponding weight, and then adds the bias
output = (
    [
        inputs[0] * weights1[0] +
        inputs[1] * weights1[1] +
        inputs[2] * weights1[2] +
        inputs[3] * weights1[3] +
        bias1
    ],
    [
        inputs[0] * weights2[0] +
        inputs[1] * weights2[1] +
        inputs[2] * weights2[2] +
        inputs[3] * weights2[3] +
        bias2
    ],
    [
        inputs[0] * weights3[0] +
        inputs[1] * weights3[1] +
        inputs[2] * weights3[2] +
        inputs[3] * weights3[3] +
        bias3
    ],
)

# show result
print(output)