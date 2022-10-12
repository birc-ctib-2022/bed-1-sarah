# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import pytest
from filecmp import cmp
import os

test_input = '../data/input.bed' #We use this as our test input
expected_output = '../data/output.bed' #This is what we want the output to look like using our input
test_output = '../data/test_output.bed' #This is what our actual output will look like

cmd1 = 'echo "" > ../data/format_bed.py' #Command to create empty file
cmd2 = 'python3.10 format_bed.py ' + test_input + ' ' + test_output #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_format_bed():
    result = cmp(test_output, expected_output, shallow = True) #Comparing test- and expected output.
    assert result

# Looked at bed-1-capibaras for inspiration.