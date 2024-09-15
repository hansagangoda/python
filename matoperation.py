def createMat(a, b, mname):     #pro6.    
    for i in range(0, a):
        mname.append([])
    for i in range(0, a):
        for j in range(0, b):
            mname[i].append(0)
    return mname


def initializeOfMat(a, b, mat):
    for i in range(a):
        for j in range(b):
            print("Enter for matrix value in row", i + 1, "and col", j + 1)
            mat[i][j] = int(input())
    return mat


def display(a, b, mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=" ")
        print()


def additionOfMat(a, b, mat1, mat2):
    result = []
    result = createMat(a, b, result)
    for i in range(a):
        for j in range(b):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result


def maltiplicatrionOfMat(a, b, mat1, mat2):
    result = []
    result = createMat(a, b, result)
    for i in range(a):
        for j in range(b):
            for k in range(a):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result