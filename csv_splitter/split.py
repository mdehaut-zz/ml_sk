#!/usr/bin/env python

"""
Splits a CSV file into multiple pieces.

Example usage:
    >> python split.py

"""

import csv
import sys
import os

############
# PARAMETERS
############
inputFile = 'train.csv'
nbrOfRows = 100000
nbrOfFiles = 2
useHeader = True
############

currentRow = 0

with open(inputFile) as infile:
    reader = csv.reader(infile, delimiter=',')
    header = next(reader)
    
    for fileCounter in range(0, nbrOfFiles):

        with open('output_{}.csv'.format(fileCounter), 'w+', newline='') as outfile:                
            writer = csv.writer(outfile, delimiter=',')
            if (useHeader):
                writer.writerow(header)

            for i, row in enumerate(reader):
                if (i >= currentRow):
                    if ((i+1) <= (nbrOfRows * (fileCounter + 1))):
                        writer.writerow(row)
                    else:
                        currentRow = nbrOfRows * (fileCounter + 1)
                        break

print('DONE & DUSTED')