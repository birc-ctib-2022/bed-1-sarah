# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import pytest
from filecmp import cmp
import os

# My BED file used for tests
bed = 'data/large.bed'

# List of query files used for tests
query = ['data/query-1.txt', 'data/query-2.txt', 'data/query-3.txt']

# List of expected outcomes for tests
expected = ['data/expected-1.txt', 'data/expected-2.txt', 'data/expected-3.txt']

# List of acctual outcome for tests
output = ['data/test-output-1.bed', 'data/test-output-2.bed', 'data/test-output-3.bed']

# Creating the outcome files for the tests with a while loop
i = 0
while i<3:
    cmd1 = 'echo "" >' + output[i]
    cmd2 = 'python3.10 query_bed.py ' + bed + ' ' + query[i] + ' -o ' + output[i]
    os.system(cmd1) # Calling our command to create empty file
    os.system(cmd2) # Writing output of running query_bed.py on files to output file
    i+=1

def test_query_bed0():
    result = cmp('data/test-output-1.bed', 'data/expected-1.txt', shallow = True) #Comparing test- and expected output.
    assert result

def test_query_bed1():
    result = cmp('data/test-output-2.bed', 'data/expected-2.txt', shallow = True) #Comparing test- and expected output.
    assert result

def test_query_bed2():
    result = cmp('data/test-output-3.bed', 'data/expected-3.txt', shallow = True) #Comparing test- and expected output.
    assert result