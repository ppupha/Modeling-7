import matplotlib.pyplot as plt

def graph_probability_over_time(probabilities, stabilization_time, times, probabilitiesOverTime):
    for i_node in range(len(probabilitiesOverTime[0])):
        plt.plot(times, [i[i_node] for i in probabilitiesOverTime])
        plt.scatter(stabilization_time[i_node], probabilities[i_node])

    plt.legend(['p{}'.format(i) for i in range(len(probabilities))])
    plt.xlabel('time')
    plt.ylabel('probability')
    plt.show()


if __name__ == '__main__':
    m1 = [[0, 2, 0, 3, 8], [0, 0, 3, 0, 0], [0, 4, 0, 0, 0], [0, 0, 5, 0, 2], [7, 0, 4, 0, 0]]
    m2 = [[0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3], [3, 0, 0, 0]]
    m3 = [[0, 0.7525, 0.2761], [0.1805, 0., 0.3038], [0.536,  0.9106, 0.]]
