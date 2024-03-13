# Overlap Graphs
from Bio import SeqIO
import numpy as np


# Parses the file with FASTA sequences using Biopython
def get_sequences(file):
    sequences = []
    fasta_ids = []
    for seq_record in SeqIO.parse(file, "fasta"):
        sequences.append(seq_record.seq)
        fasta_ids.append(seq_record.id)
    return sequences, fasta_ids


def adjacency(k, sequences, fasta_ids):
    adjacency_list = []
    adjacency_ids = []
    for i in range(len(sequences)):
        suffix = sequences[i][-k:]
        for j in range(len(sequences)):
            if i != j:
                prefix = sequences[j][:k]
                if prefix == suffix:
                    adjacency_list.append((sequences[i], sequences[j]))
                    adjacency_ids.append((fasta_ids[i], fasta_ids[j]))
    return adjacency_ids


file = "rosalind_grph.txt"

sequences, fasta_ids = get_sequences(file)

adjacent_pairs = adjacency(3, sequences, fasta_ids)

for pair in adjacent_pairs:
    print(pair[0], pair[1])
