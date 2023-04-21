# Rachel Qualls Subset Sum NPC Project CS 570
# Brute force solution to Subset Sum, uses Tree pruning approach 
# Creates a tree and prunes incorrect sums (sums of subsets that go over the num)
# Much faster than binary brute force

import copy

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
# rn just a brute force search with pruning!!
def subsetSum(num, set):
    # class to store information - we don't use recursion so we have to store stack data in self made ds
    class Link:
        def __init__(self, subSet, sum, pointer, prev):
            self.subSet = subSet
            self.sum = sum
            self.pointer = pointer
            self.prev = prev

        # add next largest number in the set if possible and return next link, if not return prev link
        def addNext(self):
            # if not big enough, return prev, try again
            if self.sum + cumlSet[self.pointer] < num:
                return self.prev
            # check next number
            while(self.pointer >= 0):
                newSum = self.sum + set[self.pointer]
                if newSum == num: # found a solution
                    self.subSet.append(set[self.pointer])
                    return self.subSet
                elif newSum < num: # create new link
                    newSet = copy.deepcopy(self.subSet)
                    newSet.append(set[self.pointer])
                    self.pointer -= 1
                    link = Link(newSet, newSum, self.pointer, self)
                    return link
                # point to next
                self.pointer -= 1
            return self.prev
    # sort first to save time
    set.sort()
    # create a cuml set to tell if the sum of all numbers is less than num we goal to sum to
    # used for quitting cond, speeds up
    cumlSet = []
    cumlSum = 0
    for i in set:
        cumlSum += i
        cumlSet.append(cumlSum)
    # create head link (empty) links to all other links in set
    head = Link([],0,len(set) - 1,None)
    result = head.addNext() # add greatest
    while(type(result) == Link): # while link keep going, if a list or none, we have found a solution
        result = result.addNext() # keep adding next, function takes care of computation
    if type(result) == list:
        return result
    else:
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