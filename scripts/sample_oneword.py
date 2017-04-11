#!/usr/bin/env python

"""
This script takes a list of "root words" as inputs
From these root words we create passwords according to
the trained RNN-LSTM model.
"""

import argparse
import subprocess
from subprocess import check_output

## Set up argument parser to execute from shell
parser = argparse.ArgumentParser()

parser.add_argument('-model', default='ccrackstation_model.t7')
parser.add_argument('-length', default='16')
parser.add_argument('-input_txt', default='pass.txt')
parser.add_argument('-output_txt', default='pass.out')
parser.add_argument('-beg', default='3')
parser.add_argument('-words', default='50')
parser.add_argument('-temp', default='1')

args = parser.parse_args()

## Run the 'sample.lua' script to generate passwords for each word in the input
##  text file, and create a new file to write the results.
##  NOTE: This will overrwrite any existing file with the same name
with open(args.input_txt, 'r') as f, open(args.output_txt, 'w') as g:
    for i in f:
        a = subprocess.Popen(['th', 'sample.lua', '-words', args.words, '-checkpoint', args.model, '-length', args.length, '-start_text', i.strip(), '-temperature', args.temp], stdout=subprocess.PIPE)
        for j in set(a.stdout):
            if j[:min(args.beg,len(i.strip()))] == i[:min(args.beg,len(i.strip()))]:
	        print>>g, j.strip()
	print i.strip()
