#this example shows how to compute eigen values of a matrix
from numpy import *
#initialize the matrix
n = 5
a = zeros( (n, n) )
for i in range(n):
    a[i][i] = i
    if(i>0):
        a[i][i-1] = -1 
        a[i-1][i] = -1

#print the matrix
print "The matrix is:"
for i in range(n):
    print a[i]

#compute the eigen values of the matrix
(eigvalues, eigvectors) = linalg.eig(a)
print "Its eigen values are:"
print eigvalues
