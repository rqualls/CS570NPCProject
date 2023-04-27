# CS570NPCProject

This NP Complete project focuses on the Subset Sum problem. 
It includes two brute force solutions (one using pruning and is thus much faster) and a huristic, as well as two mappings (3SAT->SubsetSum and SubsetSum->Partition) and example problems.


## Project Structure
By default, the project assumes the following directory structure:
 
    +-- problems                                                    # Formatted probelms that can be run and solved
    ¦   +-- subsetSumProblemGenerator                               # Python file that creats and formats problem files
    ¦
    ¦   +-- 3SAT->SubsetSum_mapping_demo                            # Problems that demonstrate the 3SAT->SubsetSum mapping
    ¦       +-- 3sat_exampleProblem.dat                             # 3 SAT problem to be mapped from
    ¦       +-- subsetsum_exampleProblem                            # Subset sum problem that is mapped to
    ¦
    ¦   +-- SubsetSum->Partition_mapping_demo                       # Problems that demonstrate the SubsetSum->Partition mapping
    ¦       +-- partition_exampleProblem.dat                        # Partition problem that is mapped to
    ¦       +-- subsetsum_exampleProblem.dat                        # Subset sum problem to be mapped from
    ¦
    ¦   +-- rlqualls                                                # Problems that the author (Rachel) created
    ¦       +-- subsetsum_hard_rlqualls.dat                         # Demonstrates a difficult problem that huristic gets incorrect
    ¦       +-- subsetsum_intractable_rlqualls.dat                  # Demonstrates intractable problem for brute force

    ¦   +-- *other student's code files mapping and results*        # Other student code files, mappings, and solutions
    ¦       ...
    ¦
    ¦   
    +-- 3SAT->SubsetSum.py                                          # Mapping from 3SAT to subset sum
    +-- SubsetSum->Partition.py                                     # Mapping from subset sum to partition
    ¦   
    +-- bruteForceBinary.py                                         # Brute force solution to subset sum 
    +-- bruteForcePrune.py                                          # Better brute force solution with pruning for subset sum
    +-- huristic.py                                                 # Huristic solution to subset sum
    ¦
    +-- README.md                                                   # Readme
    ¦


## Run Instructions
to run any python file:
```python3 fileName.py```

python files modify and read from files. Change what file you want it to read from or to in the code! Change the fileName var

python or python3 should be installed: https://www.python.org/downloads/

The libraries random and copy but they come with python and does not need to be installed
