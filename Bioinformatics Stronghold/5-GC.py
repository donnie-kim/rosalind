# Computing GC Content
from Bio import SeqIO

max_gc = 0

for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    c_count = seq_record.seq.count("C")
    # print(c_count)
    g_count = seq_record.seq.count("G")
    # print(seq_record.id)
    # print(seq_record.seq)
    gc_content = ((c_count + g_count) / len(seq_record.seq)) * 100
    if gc_content > max_gc:
        max_gc = gc_content
        max_gcID = seq_record.id

print(max_gcID)
print(max_gc)
