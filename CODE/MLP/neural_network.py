import numpy as np

n = 100000

inputLayerSize = 3
hiddenLayerSize = 4
outputLayerSize = 1


# This is my input bias
input_bias = np.array([[1,2,3,4]])

# This is my hidden layer bias
hlayer_bias = np.array([[5]])

# These are the data points
X = np.array([  [1,1,1],[1,0,1],[0,1,1],[0,0,1]  ] )

# These are my expected outputs
Y = np.array([  [0],[1],[1],[0]  ])

# This is my weight array for my x values
wx = np.random.uniform(size=(inputLayerSize, hiddenLayerSize))
print (wx)

# This is my weight array for my h values
wh = np.random.uniform(size=(hiddenLayerSize,outputLayerSize))
print(wh)

# This is my activation function
def activation_function(x):
	return 1/(1 + np.exp(-x))

# This is my derivative of activation function
def d_activation_function(x):
	return x * (1 - x)

# iterate n times
for i in range(n):
	# dot input array with weight array, add bias, and run through activation function
    h_array = activation_function(np.dot(X, wx)+input_bias)
    # dot H array with h weights add bias and run through activation function
    out_array = activation_function(np.dot(h_array, wh)+hlayer_bias)
    # find error in output
    error = Y - out_array

    # 
    d_out = error * d_activation_function(out_array)
    
    # 
    d_h = d_out.dot(wh.T) * d_activation_function(h_array)
    
    # update the wh array
    wh +=  h_array.T.dot(d_out)
    
    # Update the wx array
    wx +=  X.T.dot(d_h)


print('final Output')
print(out_array)