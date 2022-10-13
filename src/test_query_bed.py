# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import pytest
from filecmp import cmp
import os

def test_query_bed0():
    os.system('echo "" > data/test-output-1.bed') # Calling our command to create empty file
    os.system('python3.10 query_bed.py data/large.bed data/query-1.txt -o data/test-output-1.bed') # Writing output of running query_bed.py on files to output file
    assert cmp('data/test-output-1.bed', 'data/expected-1.txt') #Comparing test- and expected output.

def test_query_bed1():
    os.system('echo "" > data/test-output-2.bed') # Calling our command to create empty file
    os.system('python3.10 query_bed.py data/large.bed data/query-2.txt -o data/test-output-2.bed') # Writing output of running query_bed.py on files to output file
    assert cmp('data/test-output-2.bed', 'data/expected-2.txt') #Comparing test- and expected output.

def test_query_bed2():
    os.system('echo "" > data/test-output-3.bed') # Calling our command to create empty file
    os.system('python3.10 query_bed.py data/large.bed data/query-3.txt -o data/test-output-3.bed') # Writing output of running query_bed.py on files to output file
    assert cmp('data/test-output-3.bed', 'data/expected-3.txt') #Comparing test- and expected output.
