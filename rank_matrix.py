import numpy as np

A = [[4,-5,-13], [-2,3,9]]

print("Given Matrix")

print(A)

rank = np.linalg.matrix_rank(A)

rrefs = np.rref(A)


print("rannk of A = ", rank)

print("rref of A = ", rrefs)
