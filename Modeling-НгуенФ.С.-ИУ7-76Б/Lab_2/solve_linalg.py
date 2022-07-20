import numpy

def buildCoeffMatrix(matrix):
    matrix = numpy.array(matrix)
    n = len(matrix)
    res = numpy.zeros((n, n))

    for state in range(n - 1):
        for col in range(n):
            res[state, state] -= matrix[state, col]
        for row in range(n):
            res[state, row] += matrix[row, state]

    for state in range(n):
        res[n - 1, state] = 1

    return res


def buildAugmentationMatrix(count):
    res = [0 for i in range(count)]
    res[count - 1] = 1
    return numpy.array(res)


def solve(matrix):
    coeffMatrix = buildCoeffMatrix(matrix)
    augmentationMatrix = buildAugmentationMatrix(len(matrix))
    return numpy.linalg.solve(coeffMatrix, augmentationMatrix)
