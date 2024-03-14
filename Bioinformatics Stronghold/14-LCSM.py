# Finding a Shared Motif
from Bio import SeqIO


def get_sequences(file):
    sequences = []
    fasta_ids = []
    seq_records = []
    for seq_record in SeqIO.parse(file, "fasta"):
        sequences.append(str(seq_record.seq))
        fasta_ids.append(seq_record.id)
        seq_records.append(seq_record)
    return sequences, fasta_ids, seq_record


def shared_motif(data):
    # Initialize empty substring variable
    substr = ""
    # Check for atleast 2 sequences in data and a non-empty first sequence
    if len(data) > 1 and len(data[0]) > 0:
        # Iterate over indices of characters in data[0]
        for i in range(len(data[0])):
            # Iterate over possible lengths of substrings starting from index i. Iterates from 0 to len-i
            for j in range(len(data[0]) - i + 1):
                # Check if current substr (from index i to i+j) is present in all sequences x in the list
                if j > len(substr) and all(data[0][i : i + j] in x for x in data):
                    # If true, update substr
                    substr = data[0][i : i + j]
    return substr


sequences, fasta_ids, seq_records = get_sequences("rosalind_lcsm.txt")
print(shared_motif(sequences))
