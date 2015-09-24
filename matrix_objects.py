import math    

class Vector(list):

    @ShapeException
    def shapeException():
        return "Invalid dimenions"

    def shape(self):
        return len(self)

    def __add__(self, other):
        if len(self) != len(other):
            return "Invalid dimensions"
        for i in range(len(self)):
            self[i] += other[i]
        return self

    def __sub__(self, other):
        if len(self) != len(other):
            return "Invalid dimensions"
        for i in range(len(self)):
            self[i] -= other[i]
        return self

    def dot(self, other):
        dot_product = 0
        for x in range(len(self)):
            dot_product += self[x] * other[x]
        return dot_product

    def magnitude(self):
        return Vector.dot(self, self) ** 0.5

    def vec_mult(self, scalar):
        product = []
        for x in range(len(self)):
            product.append(self[x] * scalar)
        return product

    def mean(self, other):
        mean = []
        for x in range(len(self)):
            mean.append((self[x] + other[x])/2)
        return mean

a = [1, 2, 3, 4, 5, 6]
b = [12, 11, 10, 9, 8, 70]
c = [5, 10, 15, 20, 25, 30]

testV = Vector(a)
testV8 = Vector(b)
testV9 = Vector(c)
print(testV9 + testV + testV8)
print(Vector.magnitude(a))
print(Vector.mean(a, c))
print(testV.vec_mult(3))



class Matrix(Vector):

    def shape(self):
        return len(self[0]), len(self)

    def get_row(self, row):
        return self[row]

    def get_column(self, column):
        L = []
        for x in self:
            L.append(x[column])
        return L

    def scalar_mult(self, scalar):
        for a in range(len(self)):
            self[a] = Vector.vec_mult(self[a], scalar)
        return self

    def mat_vec_mult(self, vector):
#        if Vector.shape(vector) != self.shape()[1]:
#            return "Invalid dimensions"
        output = []
        for z in range(len(self)):
            output.append(Vector.dot(vector, self[z]))
        return output


s = [[1,2,3], [4,5,6], [5,2,7], [14,0,9]]
t = [[7,8,9], [10,11,12]]
vec = [10, 20, 30]

testM = Matrix(s)
testM8 = Matrix(t)

print(len(s))
print(Vector.shape(vec))
print(testM.shape()[1])
print(testM.get_row(2))
print(testM.get_column(1))
print(testM.scalar_mult(4))
print(testM.mat_vec_mult(vec))
