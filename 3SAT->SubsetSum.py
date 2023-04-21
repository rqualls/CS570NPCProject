# Rachel Qualls Subset Sum NPC Project CS 570
# Maps a 3SAT problem to a Subset Sum problem in the given format
# Put 3SAT problem file name in readFile and resulting Subset Sum problem file name in writeFile
# Since there is no specified formatting for answers/ solutions the program does not map the solutions only the problem
# However the source below gives a way to map solutions
# Reduction from: https://www.cs.cornell.edu/courses/cs4820/2015sp/notes/reduction-subsetsum.pdf

# change name files read to and from
readFile = "subsetsum_rlqualls.dat"
writeFile = "partition.dat"

# name files read to and from used in the program
readFileName = "problems/" + readFile
writeFileName = "problems/" + writeFile

# open files
source = open(readFileName, "r")
sink = open(writeFileName, "w")

# extract problem from read file and put problem in prob array
line = source.readline()
prob = []

while(line):
  if line.strip() == "$":
    break
  # make 2d array or 1d array of clusters
  cluster = []
  arr = (line.strip()).split(' ')
  # represent true (positive) with 1 and false (negitive) with 0
  for num in arr:
    if int(num) > 0:
      cluster.append(1)
    if int(num) < 0:
      cluster.append(0)
  # append each cluster to the problem
  prob.append(cluster)
  line = source.readline()

# where we will put the subset of numbers
subset = []

# create a and b for each var in the 3SAT problem
# add them to the subset
for i in range(3):
  a = 10 ** (len(prob) + i + 1)
  b = 10 ** (len(prob) + i + 1)
  for j in range(len(prob)):
    a += prob[j][i] * (10 ** (j + 1))
    b -= (prob[j][i] - 1) * (10 ** (j + 1))
  subset.append(a)
  subset.append(b)

# create and append c and d
for i in range(len(prob)):
  c = d = 10 ** (i + 1)
  subset.append(c)
  subset.append(d)
  
# generate m (the sum)
m = 0
for i in range(3):
  m += 10 ** (len(prob) + i + 1)
for i in range(len(prob)):
  m += 3 * (10 ** (i + 1))

# write sum to file
sink.write(str(m))
sink.write("\n")

# write set to file
for dat in subset:
  sink.write(str(dat) + " " + str(dat))
  sink.write("\n")
sink.write("$\n")

# close files
source.close()
sink.close()

print("3SAT problem from", readFile , "reduced to Subset Sum problem in", writeFile)