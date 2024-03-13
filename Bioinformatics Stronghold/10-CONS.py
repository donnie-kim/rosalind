# Consensus and Profile
from Bio import SeqIO
import numpy as np


def get_sequences_per_nt(file):
    sequences = []
    for seq_record in SeqIO.parse(file, "fasta"):
        sequences.append(seq_record)
    sequences_array = np.array(sequences)

    return sequences_array


def profile(file):
    sequences_array = get_sequences_per_nt(file)
    A = list()
    T = list()
    C = list()
    G = list()
    # print(len(sequences_array[0]))
    for i in range(len(sequences_array[0])):
        sub_array = sequences_array[:, i : i + 1]
        a_count = np.count_nonzero(sub_array == "A")
        t_count = np.count_nonzero(sub_array == "T")
        c_count = np.count_nonzero(sub_array == "C")
        g_count = np.count_nonzero(sub_array == "G")
        A.append(a_count)
        T.append(t_count)
        C.append(c_count)
        G.append(g_count)
    profile_matrix = [A, C, G, T]
    return profile_matrix


def consensus_sequence(file):
    profile_array = np.array(profile(file))
    nucleotides = ["A", "C", "G", "T"]
    max_indices = np.argmax(profile_array, axis=0)
    consensus = "".join(nucleotides[i] for i in max_indices)
    return consensus


file = "rosalind_cons.txt"
print(consensus_sequence(file))
print("A:", *profile(file)[0])
print("C:", *profile(file)[1])
print("G:", *profile(file)[2])
print("T:", *profile(file)[3])
