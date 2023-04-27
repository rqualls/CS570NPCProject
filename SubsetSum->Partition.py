# Rachel Qualls Subset Sum NPC Project CS 570
# Maps a Subset Sum problem to a Partition problem in the given format
# Put Subset Sum problem file name in readFile and resulting Partition problem file name in writeFile
# Since there is no specified formatting for answers/ solutions the program does not map the solutions only the problem
# However the source below gives a way to map solutions
# reduction from: https://www.cs.cmu.edu/~arielpro/15251/Recitations/recitation07.pdf

# !change name files read to and from
readFile = "SubsetSum->Partition_mapping_demo/subsetsum_exampleProblem.dat"
writeFile = "SubsetSum->Partition_mapping_demo/partition_exampleProblem.dat"

# name files read to and from used in the program
readFileName = "problems/" + readFile
writeFileName = "problems/" + writeFile

# open files
source = open(readFileName, "r")
sink = open(writeFileName, "w")

# read problem data sum into sumT and set into sset
sumT = int((source.readline()).strip())
line = source.readline()
sset = []

while(line):
  if line.strip() == "$":
    break
  sset.append(int(((line.strip()).split(' '))[0]))
  line = source.readline()

# add a number to the set
sset.append(2 * sumT- sum(sset))

# write data to file
for dat in sset:
  sink.write(str(dat))
  sink.write("\n")
sink.write("$\n")

# close files
source.close()
sink.close()

print("Subset Sum problem from", readFile , "reduced to Partition problem in", writeFile)