
import numpy as np
# This script is used for removing the atoms within 3AA from the ligand
# We first need the index of these atoms (index_0) calling from outputjunk file which
# is generated from the vmd console (in the bash format)
#==========================================
# #!/bin/bash
# setup_define() {
# cat << %EOF% > non_interactive_define.def
# mol new {./71_p8A_np7A.xyz} type {xyz}
# set water3aa [atomselect top "same residue as (solvent within 3 of protein)"]
# \$water3aa num
# \$water3aa get index
# %EOF%
# }
# setup_define
# vmd -e < non_interactive_define.def > outputjunk
#==========================================
# And the output file is new_pot.pot
import glob
path = "*.pot"
for filename in glob.glob(path):
    # x = ''.join(open(filename).readlines()) # Use env.pot as input file name
    with open (filename, "r") as orig_pot:
        lines = orig_pot.readlines()

def read_idx():  
    indexes = []
    with open("outputjunk", "r") as index_file:
        li = index_file.readlines()
        indexes_0 = li[-5]                     # read the 5th from the last line
        num_list = indexes_0.split(' ')
        indexes = [int(x)+3 for x in num_list] # +3 since we need to include also the first 3 lines of the original pot file
        return indexes

def new_pot():
    """_To delete all QM waters according to the index_0 list
    """
    for filename in glob.glob(path):
        x = ''.join(open(filename).readlines()) # Use env.pot as input file name
    # x = ''.join(open("test.txt").readlines())
    with open("new_pot.pot", "w") as new_pot:
        idx = x.find('@COORDINATES')           # find th pattern
        n = int(x[idx:].split('\n')[1])        # find number of atoms = lines to read
        lines[idx+1] = str(n - len(indexes)) + "\n" # new number of atoms =  old - removed atoms
        for number, line in enumerate(lines[:n+3]):
            if number not in indexes:
                new_pot.write(line)

    with open("new_pot.pot", "a") as new_pot:    
        idx = x.find('@COORDINATES')
        n = int(x[idx:].split('\n')[1])
        lines[idx + n + 5] = str(n - len(indexes)) + "\n" 
        for number, line in enumerate(lines[n+3:]):
            if number not in indexes:
                new_pot.write(line)

indexes = read_idx()    
new_pot()














