from __future__ import print_function
from enum import Enum
import sys
import hmmAlgorithms as hmm
from Bio import SeqIO
from helpers import printMatrix, printMatrixV


states = ['1', '2', '3', '4']
emissions = {'1': {'A': 0.3, 'C': 0.17, 'G': 0, 'T': 0.5},
             '2': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
             '3': {'A': 0, 'C': 0.1875, 'G': 0.0625, 'T': 0.75},
             '4': {'A': 0.8, 'C': 0.1, 'G': 0.1, 'T': 0}}
transitions = {
    ('1', '1'): 0.4,
    ('1', '2'): 0.4,
    ('1', '3'): 0.2,
    ('2', '2'): 0.6,
    ('2', '3'): 0.4,
    ('3', '3'): 0.4,
    ('3', '4'): 0.6,
    ('4', '4'): 0.5,
    ('4', '1'): 0.5
}


# check probability values
assert hmm.checkTransitions(states, transitions) != 'error'
assert hmm.checkEmissions(states, emissions) != 'error'

if __name__ == "__main__":

    filepath = sys.argv[-1]
    sequences = list(SeqIO.parse(filepath, "fasta"))
    for i, v in enumerate(range(len(sequences))):
        sequence = sequences[v].seq
        print("Seq", i+1, ":", sequence)
        F = hmm.forward(states, transitions, emissions, sequence)
        printMatrix(F, states, sequence)
        print('\n')
        F, FP = hmm.viterbi(states, transitions, emissions, sequence)
        # printMatrix(F, states, sequence)
        # print('\n')
        printMatrixV(FP, states, sequence)
        print('\n')
        path = hmm.traceback(states, FP)
        print(path)
        print('- '+' '.join(sequence)+' -')
