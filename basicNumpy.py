import numpy as np

# Virtual Environments
#   python3 -m venv .nameOfVE
#   source .nameOfVE/bin/activate
#   deactivate

# Arrays
#   unidimensional
a = np.array([1,2,3])
# a.dtype implicit and explicit
# a.shape
#   multisimensional
a2 = np.array([[1,2,3],[4,5,6]])
#       a.reshape()
#       a2.flatten()

# Special array functions
#   zeros()
#   ones()
#   full()
#   eye()
#   random.random()

# Slicing
#   Subarrays
#   Slices and integers
#   Indexing with integer arrays
#   arange()

# Boolean arrays
#   Indexing with boolean arrays

# Mathematical operations
#   operators +, -, *, /, sqrt() - element by element
#   Matrix multiplication .dot(x,y)
#       x,y vectors of size n -> scalar result
#       x matrix of size (m,n) and y vector (n,) -> y is considered size (1,n)
#       short notation: x.dot(y)

# Other operations
#   np.sum(A, axis=0/1) -> A = matrix, 0 = column and 1 = row
#   trigonometry functions: sin(), cos()
#   logarithmic and exponential functions: log(), exp()
#   transpose of matrix A.T

# Linear Algebra
#   trace(), linalg.matrix_rank(), linalg.det(), linalg.inv(), linalg.pinv()
#   Norms: 
#       L1-norm of vector x: linalg.norm(x,1)
#       L2-norm of vector x: linalg.norm(x)
#       Frobenius norm of matrix A: linalg.norm(A)
#   Cholesky descomposition (L*L^T=A): L = linalg.cholesky(A)
#   SVD descomposition (U*S*V^T=A)> U, S, V = linalg.svd(A), S = np.diag(S)
#   Eigen values (lb) and eigen vectors (v) (Av = lb*v): lb, v = linalg.eig(A)

# Broadcasting
#   empty_like(), tile(x, (a,b)), a = repeated rows and b = repeated columns
#   universal functions