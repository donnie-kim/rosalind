def point_mutations(s, t):
    hamming_distance = 0
    for i in range(len(s)):
        if t[i] != s[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance


fhand = open("rosalind_hamm.txt", "r")
seqs = list()

for line in fhand:
    line = line.rstrip()
    seqs.append(line)

seq1 = seqs[0]
seq2 = seqs[1]

hamming = point_mutations(seq1, seq2)
print(hamming)
