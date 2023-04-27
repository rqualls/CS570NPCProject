# Rachel Qualls Subset Sum NPC Project CS 570
# Maps a 3SAT problem to a Subset Sum problem in the given format
# Put 3SAT problem file name in readFile and resulting Subset Sum problem file name in writeFile
# Since there is no specified formatting for answers/ solutions the program does not map the solutions only the problem
# However the source below gives a way to map solutions
# Reduction from: https://www.cs.cornell.edu/courses/cs4820/2015sp/notes/reduction-subsetsum.pdf

# !change name files read to and from
readFile = "3SAT->SubsetSum_mapping_demo/3sat_exampleProblem.dat"
writeFile = "3SAT->SubsetSum_mapping_demo/subsetsum_exampleProblem.dat"

# name files read to and from used in the program
readFileName = "problems/" + readFile
writeFileName = "problems/" + writeFile

# open files
source = open(readFileName, "r")
sink = open(writeFileName, "w")

# extract problem from read file and put problem in prob array
max = int((source.readline()).strip())
line = source.readline()
prob = []

while(line):
  if line.strip() == "$":
    break
  # make 2d array or 1d array of clusters
  cluster = [None] * (max + 1)
  # convert to int
  strarr = (line.strip()).split(' ')
  arr = [int(numeric_string) for numeric_string in strarr]
  # represent true (positive) with 1 and false (negitive) with 0
  for num in arr:
    if int(num) > 0:
      cluster[abs(num)] = 1
    if int(num) < 0:
      cluster[abs(num)]  = 0
  # append each cluster to the problem
  prob.append(cluster)
  line = source.readline()

# where we will put the subset of numbers
subset = []

# create a and b for each var in the 3SAT problem
# add them to the subset
for i in range(1,max + 1):
  a = 10 ** (len(prob) + i)
  b = 10 ** (len(prob) + i)
  for j in range(len(prob)):
    if prob[j][i] is not None:
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
for i in range(1,max + 1):
  m += 10 ** (len(prob) + i)
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