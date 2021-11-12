#!/usr/local/bin/python3
import os, sys, re, numpy as np
import pandas as pd
os.system("wget -qO eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")
df = pd.read_csv('eukaryotes.tsv', sep="\t", na_values=['-'])
df.index=df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)
len( df[ (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ] )
big_fungi = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
sorted(list(big_fungi['#Organism/Name']))
