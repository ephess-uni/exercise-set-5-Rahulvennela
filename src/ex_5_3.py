""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import argparse 

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='ArgumentParser file')
    parser.add_argument('infile',help='Positional Argument-->INFile')
    parser.add_argument('outfile',help='Positional Argument-->OUTFile')
    args=parser.parse_args()
    raw_data = np.loadtxt(args.infile)
    raw_data-=raw_data.mean()
    x=raw_data.std()
    processed=raw_data/x
    np.savetxt(args.outfile, processed, fmt='%.2e')
