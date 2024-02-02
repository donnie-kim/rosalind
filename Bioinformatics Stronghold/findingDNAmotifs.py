def motif_counter(seq, sub):
    count = 0
    start = 0
    indexes = list()
    while start < len(seq):
        pos = seq.find(sub, start)
        if pos != -1:
            start = pos + 1
            count += 1
            indexes.append(str(start))
        else:
            break
    return " ".join(indexes)


file = open("rosalind_subs.txt", "r")
s = file.readline().strip()
t = file.readline().strip()

print(motif_counter(s, t))
