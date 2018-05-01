# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		# calculate activation which could be neg or pos
		activation += weights[i + 1] * row[i]
	print(str(activation))
	return 1.0 if activation >= 0.0 else 0.0

# test predictions
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

# starting weights will be 0, 0, 0
weights = [0, 0, 0]
l_rate = 1
epochs = 3

for i in range(epochs):
	for row in dataset:
		# define expected and predicted for each line
		expected = row[-1]
		predicted = predict(row, weights)
		# if the datapoint is misclaissiied adjust weights
		print('predicted: '+ str(predicted) + ' vs expected: '+str(expected))
		if expected != predicted:
			if expected > predicted:
				sign = 1
			else:
				sign = -1
			# get the sign of the above comparison
			weights[0] = weights[0] + sign*l_rate*1
			for i in range(len(row)-1):
				weights[i+1] = weights[i+1] + sign*l_rate*row[i]
		# print(str(weights))
