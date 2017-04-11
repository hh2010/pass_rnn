#!/usr/bin/env python

""" Script to generate passwords from the trained RNN-LSTM model """

import argparse
import subprocess
from subprocess import check_output

## Set up argument parser to execute from shell
parser = argparse.ArgumentParser()

parser.add_argument('-model', default='crackstation_model.t7')
parser.add_argument('-length', default='750000')
parser.add_argument('-output_txt', default='rand_pass_x.txt')
parser.add_argument('-beg', default='3')
parser.add_argument('-words', default='50')
parser.add_argument('-temp', default='0.9')
parser.add_argument('-rng', default=1)

args = parser.parse_args()

## Run the 'sample.lua' script to generate password lists and append them to the specific text file
with open(args.output_txt, 'a') as g:
    for i in range(1, int(args.rng)+1):
        a = subprocess.Popen(['th', 'sample.lua', '-checkpoint', args.model, '-length', args.length, '-temperature', args.temp], stdout=subprocess.PIPE)
        for j in set(a.stdout):
	    print>>g, j.strip()
	print i
