# Complementing a Strand of DNA
from Bio.Seq import Seq

fhand = open("rosalind_revc.txt", "r")
dna = Seq(fhand.read())
# dna = Seq('AAAACCCGGT')
rc = dna.reverse_complement()
print(rc)
