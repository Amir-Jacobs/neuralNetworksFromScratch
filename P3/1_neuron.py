# each neuron has inputs, weights and a bias
inputs = [2, 4.5, 1, 7]

weights = [
    [0.5, 1.0, 0.3, 0.9],
    [0.1, 0.9, 0.4, 0.2],
    [0.6, 0.2, 0.1, 0.8]
]

biases = [2, 1, 4]

# the output sums each input with its corresponding weight, and then adds the bias
layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    
    # loop through each corresponding weight and input
    for neuron_weight, neuron_input in zip(neuron_weights, inputs):
        neuron_output += neuron_weight * neuron_input

    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

# show result
print(layer_outputs)