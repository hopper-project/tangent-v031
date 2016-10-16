# Author:       Matt Bonakdarpour
# Date:         10/16/2016
# Description:  organize tuples from mathindex.cpp

import argparse
import os.path
import re

def main():
    parser = argparse.ArgumentParser(description='Hopper Tuple Post-Processing')

    parser.add_argument('--eq_paths', type=argparse.FileType('r'))
    parser.add_argument('--all_tuples', type=argparse.FileType('r'))
    parser.add_argument('--outdir', type=str)

    args = parser.parse_args()  

    eq_numbers = [os.path.basename(x.strip('\n')).strip('.mml') 
                                    for x in args.eq_paths.readlines()]
    tuples     = [x.strip('\n') for x in args.all_tuples.readlines()]

    eqNum_to_tuples ={k:[] for k in eq_numbers}
    print("Processing {} tuples".format(len(tuples)))
    for t in tuples:
        tlist = t.split('\t')
        eqtuple = eqNum_to_tuples[eq_numbers[int(tlist[0])]]
        eqtuple.append(tlist[2])
    
    odir = args.outdir
    if not os.path.exists(odir):
        os.makedirs(odir)
    
    for eq in eq_numbers:
        eq_dir = os.path.join(odir, re.search('(.*)\..*\.', eq).group(1))
        if not os.path.exists(eq_dir):
            os.makedirs(eq_dir)
        with open(os.path.join(eq_dir, eq + '.tpl'), 'w') as of:
            for t in eqNum_to_tuples[eq]:
                of.write(t + '\n')

if __name__ == "__main__":
    main()
