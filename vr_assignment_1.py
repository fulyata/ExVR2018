import math
class TMatrix:
    def __init__(self, matrix_4x4=None):
        if matrix_4x4 == None:
            # create a identity matrix, if no parameters are given
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
        """ result[0] = A[0] * B[0] + A[4] * B[1] + A[8] * B[2] + A[12] * B[3]
        result[1] = A[1] * B[0] + A[5] * B[1] + A[9] * B[2] + A[13] * B[3]
        result[2] = A[2] * B[0] + A[6] * B[1] + A[10] * B[2] + A[14] * B[3]
        result[3] = A[3] * B[0] + A[7] * B[1] + A[11] * B[2] + A[15] * B[3]

        result[4] = A[0] * B[4] + A[4] * B[5] + A[8] * B[6] + A[12] * B[7]
        result[5] = A[1] * B[4] + A[5] * B[5] + A[9] * B[6] + A[13] * B[7]"""

        for i in range(4):
            result[i * 4 + 0] = A[0] * B[i * 4] + A[4] * B[i * 4 + 1] + A[8] * B[i * 4 + 2] + A[12] * B[i * 4 + 3]
            result[i * 4 + 1] = A[1] * B[i * 4] + A[5] * B[i * 4 + 1] + A[9] * B[i * 4 + 2] + A[13] * B[i * 4 + 3]
            result[i * 4 + 2] = A[2] * B[i * 4] + A[6] * B[i * 4 + 1] + A[10] * B[i * 4 + 2] + A[14] * B[i * 4 + 3]
            result[i * 4 + 3] = A[3] * B[i * 4] + A[7] * B[i * 4 + 1] + A[11] * B[i * 4 + 2] + A[15] * B[i * 4 + 3]
      
        return TMatrix(result)

        def mult_vec(self, vector):
            pass

    def __str__(self):
        return "[{: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f};\n {: 10.4f}, {: 10.4f}, {: 10.4f}, {: 10.4f}]".format(
            self.matrix_4x4[0], self.matrix_4x4[4], self.matrix_4x4[8], self.matrix_4x4[12],
            self.matrix_4x4[1], self.matrix_4x4[5], self.matrix_4x4[9], self.matrix_4x4[13],
            self.matrix_4x4[2], self.matrix_4x4[6], self.matrix_4x4[10], self.matrix_4x4[14],
            self.matrix_4x4[3], self.matrix_4x4[7], self.matrix_4x4[11], self.matrix_4x4[15])
    
# Free standing functions
def make_trans_mat(x, y, z):
    trans_mat = TMatrix([[1, 0, 0, x], # coloumn 1
                        [0, 1, 0, y], # coloumn 2
                        [0, 0, 1, z],
                        [0, 0, 0, 1]])
    return trans_mat

def make_rot_mat(degree, axis):
    rad = math.radians(degree)
    if axis == 'x':
        rot_mat_x = TMatrix([[1.0, 0.0, 0.0, 0.0],
                            [0.0, math.cos(rad), math.sin(rad), 0.0],
                            [0.0, -math.sin(rad), math.cos(rad), 0.0],
                            [0.0, 0.0, 0.0, 1.0]])
        return rot_mat_x
    elif axis == 'y':
        rot_mat_y = TMatrix([[math.cos(rad), 0.0, -math.sin(rad), 0.0],
                            [0.0, 1.0, 0.0, 0.0],
                            [math.sin(rad), 0.0, math.cos(rad), 0.0],
                            [0.0, 0.0, 0.0, 1.0]])
        return rot_mat_y
    elif axis == 'z':
        rot_mat_z = TMatrix([[math.cos(rad), math.sin(rad), 0, 0],
                            [-math.sin(rad), math.cos(rad), 0,0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
        return rot_mat_z

def make_scale_mat(sx, sy, sz):
    scale_mat = TMatrix([[sx, 0, 0, 0],
                        [0, sy, 0, 0],
                        [0, 0, sz, 0],
                        [0, 0, 0, 1]])
    return scale_mat

class Vector4:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

# Testing
#print("-----Exercise 1.1-----")
A = TMatrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
B = TMatrix()
print(A)
print(B)

print(A.mult(B))
# print("-----Exercise 1.2-----")
# print("This is your translation matrix")
# print(make_trans_mat(1, 2, 3))
# print("These are your rotation matrices")
# print(make_rot_mat(45, 'x'))
# print(make_rot_mat(90, 'y'))
# print(make_rot_mat(120, 'z'))
# print("This is your scaling matrix")
# print(make_scale_mat(1, 2, 3))

