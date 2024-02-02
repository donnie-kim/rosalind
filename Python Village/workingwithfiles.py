"""

"""

fhand = open("rosalind_ini5.txt")
fout = open("workingwithfiles.txt", "w")
count = 1
for line in fhand:
    line = line.strip()
    if count % 2 == 0:
        # print(line)
        fout.write(line + "\n")
    count = count + 1
    # print(line)
