import numpy as np

# Testing creation of numpy arrays as well as printing them to see the effect
a = np.array([4, 5, 6])
print(a)

b = np.array([a, [2, 1, 3], [5, 4, 1]])
print(b)

# Testing the get dimension method
print(a.ndim)
print(b.ndim)

# Testing the shape method, in our case b is a 3 by 3 matrix, hence (3, 3)
print(b.shape)

# Testing get type method
print(a.dtype)
c = np.array([1, 2], dtype='int16')
print(c.dtype)

# Testing item size and number of bytes methods
print(a.itemsize)
print(a.nbytes)\

# Learning how to access/change speciic elements, rows , columns etc.
d = np.array([[121, 123, 21, 312, 12], [312, 968, 123, 84, 12]])
print(d)
print('trying to access 968')
print(d[1, 1])
# get specific row
print(d[1, :])
# get specific column
print(d[:, 2])
# being a bit more selective with the accessing [startindex:endindex:stepsize]
print(d[0, 1:5:1])
# changing values
d[0,0] = 212
print(d)
d[0,:] = 666
print(d)

# testing 3d arrays
f = np.array([[[123, 312], [1, 2]], [[43, 12], [123, 92]]])
print(f'\n{f}')
# accessing elements
print(f[0, 1, 0])
print('\n')
for index1 in range(2):
    for index2 in range(2):
        for index3 in range(2):
            print(f[index1, index2, index3])


# initializing all zero matrix
g = np.zeros((2,2))
print(g)
# now all ones matrix
g = np.ones((3,3))
print(g)
#some other number matrix
g = np.full((2,2), 666)
print(g)

# identity matrix
o = np.identity(5)
print(o)

# creating a complicated matrix
y = np.ones((5,5))
y[1:4, 1:4] = 0
y[2,2] = 9
print(f'\n{y}')

# testing maths
p = np.array([2, 3, 1])
print(p)
print(p+2)
print(p/2)
print(p*3)
print(p**4)
print(np.sin(p))

# doing some linear algebra
a = np.full((2, 3), 6)
print(a)
b = np.full((3,2), 2)
print(b)
print(np.matmul(a, b))
print(np.linalg.det(np.matmul(a, b)))

# statistics
s = np.array([[123, 123], [512, 122]])
print(np.mean(s))
print(np.max(s))
print(np.sum(s))
print(np.max(s, axis=0))
print(np.sum(s, axis=1))

