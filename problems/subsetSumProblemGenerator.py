# Rachel Qualls Subset Sum NPC Project CS 570
# Creates Subset Sum random problems of the specified format
# Fill in the inputs under ** to create unique random problems

import random

# **Input the following presets to generate problem
# Name of file problem will be written in
fileName = "subsetsum_exampleProblem.dat"
# size of set
size = 50
# max int to sum to
maxSum = 10000
# max int to each num in the set can be
maxNum = 500

# num we want to sum to
sum = random.randint(0,maxSum)

# init vals in set
set = []

# make set
for i in range(size):
    rnum = random.randint(0,maxNum)
    set.append(rnum)

file = open(fileName, "w")

# write sum to file
file.write(str(sum))
file.write("\n")

# write set to file
for dat in set:
  file.write(str(dat) + " " + str(dat))
  file.write("\n")
file.write("$\n")

# close file
file.close()

print("Subset Sum problem written in", fileName)