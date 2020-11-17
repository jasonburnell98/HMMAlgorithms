from __future__ import print_function


def initializeMatrix(seq1, seq2, value=0):
    F = []
    for i in range(0, seq1):
        F.append([])
        for j in range(0, seq2):
            F[i].append(value)
    return F


def printMatrix(matrix, hinge1, hinge2):
    w = '{:<10}'
    print(w.format('') + w.format('0') +
          ''.join([w.format(char) for char in hinge2]) + w.format('0'))
    for i, row in enumerate(matrix):
        print(w.format(hinge1[i]) +
              ''.join(['{:<10.2e}'.format(item) for item in row]))


def printMatrixV(matrix, hinge1, hinge2):
    w = '{:<10}'
    print(w.format('') + w.format('0') +
          ''.join([w.format(char) for char in hinge2]) + w.format('0'))
    for i, row in enumerate(matrix):
        print(w.format(hinge1[i]) +
              ''.join(['{:<10s}'.format(item) for item in row]))


def maxValue(values):
    maxVal = values[0]
    maxIndex = 0
    for ind, val in enumerate(values):
        if val > maxVal:
            maxVal = val
            maxIndex = ind
    return maxVal, maxIndex
