import numpy as np

x = np.array([  [1,1,1],[1,0,1],[0,1,1],[0,0,1]  ] )

y = np.array([  [0],[1],[1],[0]  ])

w = np.array([  [1,1,1,1],[1,1,1,1],[1,1,1,1]  ] )

b = np.array( [  1,1,1,1  ] )

print(x)
print(y)
print(w)
print(b)


def activation_function(x):
	# This is our activation function
	activation_value = 1/(1+np.exp(x))
	return activation_value

x_dot_w = np.dot(x,w)

print ('scalar multiply x and w')

print(x_mult_w)

input_function = np.array(np.sum(x_mult_w, axis = 1))

print('X mult with W'  + str(input_function))

input_function = input_function + b

print('Sum of wx and b ' + str(input_function))

input_function = np.sum(input_function, axis = 0)

print('Input Output is: ' + str(input_function))

print ('Activation Output is: ' + str(activation_function(input_function)))