import math
class TMatrix:
    def __init__(self, matrix_4x4=None):
        if matrix_4x4 == None:
            # create a identity matrix, if no parameters are given
            # the order of the matrices created are in column-major order
            self.matrix_4x4 = [1, 0, 0, 0, 
                               0, 1, 0, 0,
                               0, 0, 1, 0,
                               0, 0, 0, 1]
        else:
            # create a matrix in column-major order
            self.matrix_4x4 = matrix_4x4

    def mult(self, other_matrix):
        # multiply 
        if type(self) != type(other_matrix):
            print("The matrix is not in the dimention 4x4, please enter a 4x4 matrix")

        result = [0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0]
        A = self.matrix_4x4
        B = other_matrix.matrix_4x4

        for i in range(4):
            result[i * 4 + 0] = A[0] * B[i * 4] + A[4] * B[i * 4 + 1] + A[8] * B[i * 4 + 2] + A[12] * B[i * 4 + 3]
            result[i * 4 + 1] = A[1] * B[i * 4] + A[5] * B[i * 4 + 1] + A[9] * B[i * 4 + 2] + A[13] * B[i * 4 + 3]
            result[i * 4 + 2] = A[2] * B[i * 4] + A[6] * B[i * 4 + 1] + A[10] * B[i * 4 + 2] + A[14] * B[i * 4 + 3]
            result[i * 4 + 3] = A[3] * B[i * 4] + A[7] * B[i * 4 + 1] + A[11] * B[i * 4 + 2] + A[15] * B[i * 4 + 3]
        return TMatrix(result)

    def mult_vec(self, vector):
        result = [0, 0, 0, 0]
        A = self.matrix_4x4
        b = vector.vector
        for i in range(4):
            result[i] = A[i] * b[0] + A[i + 4] * b[1] + A[i + 8] * b[2] + A[i + 12] * b[3]
        return Vector4(result)
        

    def __str__(self):
        return "[{: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f}]".format(
            self.matrix_4x4[0], self.matrix_4x4[4], self.matrix_4x4[8], self.matrix_4x4[12],
            self.matrix_4x4[1], self.matrix_4x4[5], self.matrix_4x4[9], self.matrix_4x4[13],
            self.matrix_4x4[2], self.matrix_4x4[6], self.matrix_4x4[10], self.matrix_4x4[14],
            self.matrix_4x4[3], self.matrix_4x4[7], self.matrix_4x4[11], self.matrix_4x4[15])
    
# Free standing functions
def make_trans_mat(x, y, z):
    trans_mat = TMatrix([1, 0, 0, 0, 0, 1, 0, 0,0, 0, 1, 0, x, y, z, 1])
    return trans_mat

def make_rot_mat(degree, axis):
    rad = math.radians(degree)
    if axis == 'x':
        rot_mat_x = TMatrix([1.0, 0.0, 0.0, 0.0,
                             0.0, math.cos(rad), math.sin(rad), 0.0,
                             0.0, -math.sin(rad), math.cos(rad), 0.0,
                             0.0, 0.0, 0.0, 1.0])
        return rot_mat_x
    elif axis == 'y':
        rot_mat_y = TMatrix([math.cos(rad), 0.0, -math.sin(rad), 0.0,
                             0.0, 1.0, 0.0, 0.0,
                             math.sin(rad), 0.0, math.cos(rad), 0.0,
                             0.0, 0.0, 0.0, 1.0])
        return rot_mat_y
    elif axis == 'z':
        rot_mat_z = TMatrix([math.cos(rad), math.sin(rad), 0.0, 0.0,
                             -math.sin(rad), math.cos(rad), 0.0, 0.0,
                             0.0, 0.0, 1.0, 0.0,
                             0.0, 0.0, 0.0, 1.0])
        return rot_mat_z

def make_scale_mat(sx, sy, sz):
    scale_mat = TMatrix([sx, 0, 0, 0,
                         0, sy, 0, 0,
                         0, 0, sz, 0,
                         0, 0, 0, 1])
    return scale_mat

class Vector4:
    def __init__(self, vector=None):
        if vector is None:
            self.vector = [0, 0, 0, 0]
        else:
            self.vector = vector

    def __str__(self):
        return "[{: 10.4f}\n {: 10.4f}\n {: 10.4f}\n {: 10.4f}]".format(self.vector[0], self.vector[1], self.vector[2], self.vector[3])
    

def euclidean_distance(point1, point2):
    x_diff = (point2.vector[0] - point1.vector[0])**2
    y_diff = (point2.vector[1] - point1.vector[1])**2
    z_diff = (point2.vector[2] - point1.vector[2])**2
    w_diff = (point2.vector[3] - point1.vector[3])**2
    distance = math.sqrt((x_diff + y_diff + z_diff + w_diff))
    return distance

# Testing
print("Exercise 1.1")
A = TMatrix([1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16])
B = TMatrix([1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 16])
print(A)
print(B)
print("A * B:\n" + str(A.mult(B)))

print("Exercise 1.2")
print("Translation matrix with t_x = 1, t_y = 2, t_z = 3")
print(make_trans_mat(1, 2, 3))
print("Rotation matrix 45 degrees around x-axis")
print(make_rot_mat(45, 'x'))
print("Rotation matrix 90 degrees around y-axis")
print(make_rot_mat(90, 'y'))
print("Rotation matrix 120 degrees around z-axis")
print(make_rot_mat(120, 'z'))
print("Scaling matrix with s_x = 1, s_y = 2, s_z = 3")
print(make_scale_mat(1, 2, 3))

print("Exercise 1.3")
print("The euclidean distance between Vector4([2, 4, 6, 2]) and Vector4([0, 0, 0, 1])")
print(euclidean_distance(Vector4([2, 4, 6, 2]), Vector4([0, 0, 0, 1])))

print("Exercise 1.4")
b = Vector4([1, 2, 3, 1])
print(b)
print("A * b:\n" + str(A.mult_vec(b)))

# 1.5
# show that make_rot_mat(90, 'x') * make_rot_mat(180, 'z')
# == make_rot_mat(180, 'y') * make_rot_mat(90, 'x')
# see pdf for more info
print("Exercise 1.5")
print(make_rot_mat(90, 'x').mult(make_rot_mat(180, 'z')))
print("==")
print(make_rot_mat(180, 'y').mult(make_rot_mat(90, 'x')))

