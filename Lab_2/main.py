from math import fabs
import random
import matplotlib.pyplot as plt
import numpy

PRECISION = 5
TIME_DELTA = 1e-3
MAGIC_NUM = 10

def dps(matrix, P):
    n = len(matrix)
    res = [sum(
            [
                P[j] * (-sum(matrix[i]) + matrix[i][i]) if i == j else P[j] * matrix[j][i] for j in range(n)
            ]
        )
        for i in range(n)]
    
    return [i * TIME_DELTA for i in res]

def calcStabilizationTimes(matrix, start_P, limit_P):
    n = len(matrix)
    current_time = 0
    current_P = start_P.copy()
    stabilizationTimes = [0 for i in range(n)]

    total_lambda_sum = sum([sum(i) for i in matrix]) * MAGIC_NUM
    cool_eps = [p/total_lambda_sum for p in limit_P]

    while not all(stabilizationTimes):
        curr_dps = dps(matrix, current_P)
        for i in range(n):
            if (not stabilizationTimes[i] and curr_dps[i] <= 1e-7 and
                    abs(current_P[i] - limit_P[i]) <= cool_eps[i]):
                stabilizationTimes[i] = current_time
            current_P[i] += curr_dps[i]

        current_time += TIME_DELTA

    return stabilizationTimes


def calcPOverTime(matrix, start_P, end_time):
    n = len(matrix)
    current_time = 0
    current_P = start_P.copy()

    POverTime = []
    times = []

    while current_time < end_time:
        POverTime.append(current_P.copy())
        curr_dps = dps(matrix, current_P)
        for i in range(n):
            current_P[i] += curr_dps[i]

        current_time += TIME_DELTA

        times.append(current_time)

    return times, POverTime
    
    
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

def graphPOverTime(P, stabilizationTime, times, POverTime):
    for i_node in range(len(POverTime[0])):
        plt.plot(times, [i[i_node] for i in POverTime])
        plt.scatter(stabilizationTime[i_node], P[i_node])

    plt.legend(['p{}'.format(i+1) for i in range(len(P))])
    plt.xlabel('time')
    plt.ylabel('P')
    plt.show()
    

def random_matrix(size):
    return [
        [round(random.random(), PRECISION) if i != j else 0.0 for j in range(size)]
        for i in range(size)
    ]


def output(title, caption, data):
    print(title)
    for i in range(len(data)):
        print(caption + str(i), round(fabs(data[i]), PRECISION))
    print()


def getPreDefineI(i):
    if i == 3:
        return [[0, 2, 0],
                [1, 0, 0],
                [0, 1, 1]]
    if i == 4:
        return [[0, 2, 0, 0],
                [0, 0, 2, 3],
                [3, 0, 0, 1],
                [0, 4, 0, 0]]
    elif i == 5:
        return [[0, 1, 1, 2, 0],
                [0, 0, 0, 0, 0.5],
                [0, 2, 0, 1, 0],
                [0, 0, 3, 0, 1.5],
                [2, 0, 0, 2, 0]]


def getStartP(n, all_equal=True):
    if all_equal:
        return [1/n] * n
    else:
        res = [0] * n
        res[0] = 1
        return res


if __name__ == '__main__':
    n = 5
    #I = random_matrix(n)
    I = getPreDefineI(n)

    start_P = getStartP(n, True)

    P = solve(I)
    output('P:', 'p', P)

    stabilizationTime = calcStabilizationTimes(I, start_P, P)
    times, POverTime = calcPOverTime(I, start_P, 5)
    output('T:', 't', stabilizationTime)

    graphPOverTime(P, stabilizationTime, times, POverTime)
