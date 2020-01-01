import numpy as np

sample_data = [[0,0], [0,1], [1,0], [1,1]]
expected_results = [0,1,1,1]
activation_threshold = 0.5

weights = np.random.random(2)/1000
bias_weight = np.random.random()

for iteration_num in range(5):
    correct_answers = 0
    for idx, sample in enumerate(sample_data):
        input_vector = np.array(sample)
        weights = np.array(weights)
        activation_level = np.dot(input_vector, weights) + \
            (bias_weight * 1)
        if activation_level > activation_threshold:
            perceptron_output = 1
        else:
            perceptron_output = 0
        if perceptron_output == expected_results[idx]:
            correct_answers += 1
        new_weights = []
        for i, x in enumerate(sample):
            new_weights.append(weights[i] + (expected_results[idx] - \
                perceptron_output) * x)
        print('old weights:{}, new weights:{}'.format(weights, new_weights))

