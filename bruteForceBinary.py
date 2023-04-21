# Rachel Qualls Subset Sum NPC Project CS 570
# Brute force solution to Subset Sum, uses Binary approach 
# Goes though every combination in subset til it finds one that sums to sum

# change name files read to and from
fileName = "subsetsum1_rlqualls.dat"

# name files read to and from used in the program
readFileName = "problems/" + fileName

# open files
file = open(readFileName, "r")

# read problem data sum into num and set into set
num = int((file.readline()).strip())
line = file.readline()
set = []

while(line):
  if line.strip() == "$":
    break
  set.append(int(((line.strip()).split(' '))[0]))
  line = file.readline()

# print set
print("we want to sum to " + str(num))

print("our set is: ", end='')
for i in set:
    print(i, end=' ')
print("\n")

# solves sumset sum
# when given a set (array of ints) and num (int)
# find a subset that sums to the num
# if there is no subset that sums to num, return none
# O(n*(2^n)) time complexity
def subsetSum(num, set):
    # go though all combinations
    for i in range(2**(len(set))):
        sum = 0
        subset = []
        numb = i
        # choose which numbers in set to sum
        for n in reversed(range((len(set)))):
            if numb != 0 and numb - (2**n) >= 0:
                sum += set[n]
                subset.append(set[n])
                numb -= (2**n)
        # if equal, return
        if sum == num:
            return subset
    return None

solution = subsetSum(num, set)
print("solution: ", solution)

# close file
file.close()

# reopen file in append mode and write solution
file = open(readFileName, "a")
file.write("brute force:\n\t" + str(solution) + "\n")

# close file
file.close()
