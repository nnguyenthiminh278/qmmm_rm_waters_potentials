#!/bin/bash

setup_define() {
cat << %EOF% > non_interactive_define.def

mol new {./71_p8A_np7A.xyz} type {xyz}
set water3aa [atomselect top "same residue as (solvent within 3 of protein)"]
\$water3aa num
\$water3aa get index

%EOF%
}

setup_define

vmd -e < non_interactive_define.def > outputjunk
