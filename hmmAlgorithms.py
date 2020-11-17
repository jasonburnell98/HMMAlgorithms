import numpy as np
from helpers import initializeMatrix, maxValue


def checkTransitions(states, transitions):
    for state in states:
        if state != '4':
            pSum = 0
            for transition in transitions.keys():
                if state == transition[0]:
                    pSum += transitions[transition]
            if round(pSum, 3) != 1:
                return 'error'


def checkEmissions(states, emissions):
    for state in states:
        if state != '1' and state != '4':
            pSum = 0
            for emission in emissions[state].keys():
                pSum += emissions[state][emission]
            if round(pSum, 3) != 1:
                return 'error'


def forward(states, transitions, emissions, sequence):
    F = initializeMatrix(len(states), len(sequence)+2)
    F[0][0] = 1
    for i in range(1, len(states)-1):
        F[i][1] = transitions[(states[0], states[i])] * \
            emissions[states[i]][sequence[0]]
    for j in range(2, len(sequence)+1):
        for i in range(1, len(states)-1):
            pSum = 0
            for k in range(1, len(states)-1):
                pSum += F[k][j-1]*transitions[(states[k], states[2])] * \
                    emissions[states[i]][sequence[j-1]]
            F[i][j] = pSum
    pSum = 0
    for k in range(1, len(states)-1):
        pSum += F[k][len(sequence)]*transitions[(states[k], states[2])]
    F[-1][-1] = pSum
    return F


def viterbi(states, transitions, emissions, sequence):
    F = initializeMatrix(len(states), len(sequence)+2)
    FP = initializeMatrix(len(states), len(sequence)+2, states[0])
    F[0][0] = 1
    for i in range(1, len(states)-1):
        F[i][1] = transitions[(states[0], states[i])] * \
            emissions[states[i]][sequence[0]]
    for j in range(2, len(sequence)+1):
        for i in range(1, len(states)-1):
            values = []
            for k in range(1, len(states)-1):
                values.append(F[k][j-1]*transitions[(states[k], states[2])]
                              * emissions[states[i]][sequence[j-1]])
            maxVal, maxInd = maxValue(values)
            F[i][j] = maxVal
            FP[i][j] = states[maxInd+1]
    values = []
    for k in range(1, len(states)-1):
        values.append(F[k][len(sequence)]*transitions[(states[k], states[2])])
    maxVal, maxInd = maxValue(values)
    F[-1][-1] = maxVal
    FP[-1][-1] = states[maxInd+1]
    return F, FP


def traceback(states, FP):
    path = ['4']  # last element in path is our end state
    # current state is in the last cell of the matrix
    current = FP[-1][-1]
    for i in range(len(FP[0])-2, 0, -1):  # loops through the symbols
        path = [current] + path  # append current state with path
        current = FP[states.index(current)][i]
    path = ['1'] + path  # the first element of the path is the begin state
    # transforms list into a string, elements are separated with a space
    return ' '.join(path)
