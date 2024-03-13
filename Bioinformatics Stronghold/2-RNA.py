# Transcribing DNA into RNA
# rna = 'GATGGAACTTGACTACGTAAATT'


file = open("rosalind_rna.txt", "r")
string = file.read()
dna = string.replace("T", "U")
print(dna)
