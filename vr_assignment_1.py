import math
class TMatrix:
    def __init__(self, matrix_4x4 = None):
        if matrix_4x4 == None:
            # create the identity matrix, if no parameters are given
            self.matrix_4x4 = [[1, 0, 0, 0], #coloumn 1
                               [0, 1, 0, 0], 
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]
        else:
            self.matrix_4x4 = matrix_4x4

        def mult(self, other_matrix):
            # multiply 
            if type(self) != type(other_matrix):
                print("The matrix is not in the dimention 4x4, please enter a 4x4 matrix")

            temp_4x4 = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
            coloumns_list = [temp_4x4[0], temp_4x4[1], temp_4x4[2], temp_4x4[3]] 
            for coloumn in coloumns_list:
                for row in range (0, 4):
                    result = self.[row][coloumn] * other_matrix.[coloumn]

# Free standing functions
def make_trans_mat(x, y, z):
    trans_mat = TMatrix([1, 0, 0, x], # coloumn 1
                        [0, 1, 0, y],
                        [0, 0, 1, z],
                        [0, 0, 0, 1])
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
        rot_mat_y = TMatrix([math.cos(rad), 0.0, -math.sin(rad), 0.0],
                            [0.0, 1.0, 0.0, 0.0],
                            [math.sin(rad), 0.0, math.cos(rad), 0.0],
                            [0.0, 0.0, 0.0, 1.0])
        return rot_mat_y
    elif axis == 'z':
        rot_mat_z = TMatrix([math.cos(rad), math.sin(rad), 0, 0],
                            [-math.sin(rad), math.cos(rad), 0,0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1])
                
# Testing
A = TMatrix([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]])
B = TMatrix([[1, 9, 2, 10], [3, 11, 4, 12], [5, 13, 6, 14], [7, 15, 8, 16]])


