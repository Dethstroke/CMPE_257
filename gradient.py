import numpy as np

#np is a packagw

A = np.array([1,2,4,6], dtype=np.float)

print("Given Matrix")

print(A)

grad = np.gradient(A)


print("gradient of A = ", grad)

