from Bio.Seq import Seq

mRNA = Seq(open("rosalind_prot.txt", "r").read().strip())
aminoacid_sequence = mRNA.translate(to_stop=True)

print(aminoacid_sequence)
print(len(mRNA))
