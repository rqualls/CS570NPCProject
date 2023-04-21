# CS570NPCProject

This NP Complete project focuses on the Subset Sum problem. 
It includes two brute force solutions (one using pruning and is thus much faster) and a huristic, as well as two mappings (3SAT->SubsetSum and SubsetSum->Partition) and example problems.


## Project Structure
By default, the project assumes the following directory structure:
 
    +-- problems                                # Formatted probelms that can be run and solved
    ¦   +-- subsetsum_rlqualls.dat              # problem
    ¦   +-- subsetsum1_rlqualls.dat             # problem1
    ¦   
    +-- 3SAT->SubsetSum.py                      # Mapping from 3SAT to subset sum
    +-- SubsetSum->Partition.py                 # Mapping from subset sum to partition
    ¦   
    +-- bruteForceBinary.py                     # Brute force solution to subset sum 
    +-- bruteForcePrune.py                      # Better brute force solution with pruning for subset sum
    +-- huristic.py                             # Huristic solution to subset sum
    ¦


## Run Instructions
to run any python file:
```python3 fileName.py```
python or python3 should be installed: https://www.python.org/downloads/

The libraries random and copy but they come with python and does not need to be installed
