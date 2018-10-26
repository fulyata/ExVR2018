import math
class TMatrix:
    def __init__(self, matrix_4x4=None):
        if matrix_4x4 == None:
            # create a identity matrix, if no parameters are given
            self.matrix_4x4 = [[1, 0, 0, 0], #column 1
                               [0, 1, 0, 0], 
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]
        else:
            # create a matrix in column-major order
            self.matrix_4x4 = matrix_4x4

        def mult(self, other_matrix):
            # multiply 
            if type(self) != type(other_matrix):
                print("The matrix is not in the dimention 4x4, please enter a 4x4 matrix")

            temp_4x4 = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
            temp_4x4[0][0] = self.matrix_4x4[0][0] * other_matrix.matrix_4x4[0][0]
            temp_4x4[1][0] = self.matrix_4x4[0][0] * other_matrix.matrix_4x4[0][0]
            
            #for coloumn in coloumns_list:
            #    for row in range (0, 4):
            #        result = self.[row][coloumn] * other_matrix.[coloumn]

        def mult_vec(self, vector):
            pass

    def __str__(self):
        return "[{: 5.4f} | {: 5.4f} | {: 5.4f} | {: 5.4f}\n {: 5.4f} | {: 5.4f} | {: 5.4f} | {: 5.4f}\n {: 5.4f} | {: 5.4f} | {: 5.4f} | {: 5.4f}\n {: 5.4f} | {: 5.4f} | {: 5.4f} | {: 5.4f}]".format(
            self.matrix_4x4[0][0], self.matrix_4x4[1][0], self.matrix_4x4[2][0], self.matrix_4x4[3][0],
            self.matrix_4x4[0][1], self.matrix_4x4[1][1], self.matrix_4x4[2][1], self.matrix_4x4[3][1],
            self.matrix_4x4[0][2], self.matrix_4x4[1][2], self.matrix_4x4[2][2], self.matrix_4x4[3][2],
            self.matrix_4x4[0][3], self.matrix_4x4[1][3], self.matrix_4x4[2][3], self.matrix_4x4[3][3])
    
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

    def euclidean_distance(pt1, pt2):
        pass
    
    
# Testing
print("-----Exercise 1.1-----")
A = TMatrix([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]])
B = TMatrix([[1, 9, 2, 10], [3, 11, 4, 12], [5, 13, 6, 14], [7, 15, 8, 16]])
print(A)
print(B)

print("-----Exercise 1.2-----")
print("This is your translation matrix")
print(make_trans_mat(1, 2, 3))
print("These are your rotation matrices")
print(make_rot_mat(45, 'x'))
print(make_rot_mat(90, 'y'))
print(make_rot_mat(120, 'z'))
print("This is your scaling matrix")
print(make_scale_mat(1, 2, 3))


