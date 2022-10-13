# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import pytest
from filecmp import cmp
import os

os.system('echo "" > data/test-output-1.bed') # Calling our command to create empty file
os.system('python3.10 src/query_bed.py data/large.bed data/query-1.txt -o data/test-output-1.bed') # Writing output of running query_bed.py on files to output file

os.system('echo "" > data/test-output-2.bed') # Calling our command to create empty file
os.system('python3.10 src/query_bed.py data/large.bed data/query-2.txt -o data/test-output-2.bed') # Writing output of running query_bed.py on files to output file

os.system('echo "" > data/test-output-3.bed') # Calling our command to create empty file
os.system('python3.10 src/query_bed.py data/large.bed data/query-3.txt -o data/test-output-3.bed') # Writing output of running query_bed.py on files to output file

def test_query_bed0():
    assert cmp('data/test-output-1.bed', 'data/expected-1.txt') #Comparing test- and expected output.

def test_query_bed1():
    assert cmp('data/test-output-2.bed', 'data/expected-2.txt') #Comparing test- and expected output.

def test_query_bed2():
    assert cmp('data/test-output-3.bed', 'data/expected-3.txt') #Comparing test- and expected output.
