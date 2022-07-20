TIME_DELTA = 1e-3
MAGIC_NUM = 10


def dps(matrix, probabilities):
    n = len(matrix)
    res = [sum(
            [
                probabilities[j] * (-sum(matrix[i]) + matrix[i][i]) if i == j else probabilities[j] * matrix[j][i] for j in range(n)
            ]
        )
        for i in range(n)]
    
    return [i * TIME_DELTA for i in res]


def calcStabilizationTimes(matrix, start_probabilities, limit_probabilities):
    n = len(matrix)
    current_time = 0
    current_probabilities = start_probabilities.copy()
    stabilizationTimes = [0 for i in range(n)]

    total_lambda_sum = sum([sum(i) for i in matrix]) * MAGIC_NUM
    cool_eps = [p/total_lambda_sum for p in limit_probabilities]

    while not all(stabilizationTimes):
        curr_dps = dps(matrix, current_probabilities)
        for i in range(n):
            if (not stabilizationTimes[i] and curr_dps[i] <= cool_eps[i] and
                    abs(current_probabilities[i] - limit_probabilities[i]) <= cool_eps[i]):
                stabilizationTimes[i] = current_time
            current_probabilities[i] += curr_dps[i]

        current_time += TIME_DELTA

    return stabilizationTimes


def calcPOverTime(matrix, start_probabilities, end_time):
    n = len(matrix)
    current_time = 0
    current_probabilities = start_probabilities.copy()

    probabilitiesOverTime = []
    times = []

    while current_time < end_time:
        probabilitiesOverTime.append(current_probabilities.copy())
        curr_dps = dps(matrix, current_probabilities)
        for i in range(n):
            current_probabilities[i] += curr_dps[i]

        current_time += TIME_DELTA

        times.append(current_time)

    return times, probabilitiesOverTime
