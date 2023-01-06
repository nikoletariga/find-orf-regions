# Find ORF Regions 

## Project Goal

The goal of this project is to find ORF regions in sequences. The ORF regions start with the start codon "ATG" and stops with one of the three stop codons "TAA", "TGA", "TAG". 

This code checks the following cases:
1. The sequence has "ATG" and one of the three stop codons "TAA", "TGA", "TAG".\
In this case it prints the ORF region.
2. The sequence has only "ATG".\
In this case it prints "Start codon found, but ORF region does not exist"
3. The sequence has not "ATG".\
In this case it prints "There is not start codon."

In addition, this code:
1. Checks for multiple ORF regions in every sequence and prints the number of the ORF regions. 
2. Gives the complementary sequence.
3. Gives the reversed complementary sequence. 
4. Splits the ORF regions in triplets. 


## Requirements

To run fasta files you need:
```
pip install bio 
```

## Input

In this code the user has four different input options:

* Give your own sequence
* file.seq
* file.fasta
* file.fastq


## Acknowledgements 

The example.fasta got it from here: 
https://clana.medium.com/bioinformatics-101-reading-fasta-files-using-biopython-501c390c6820
(ls_orchid.fasta)

For the example.fastq used first 10 sequences from here:
https://www.ebi.ac.uk/ena/browser/view/SRX3166165
(SRR6012654.fastq.gz)


## Development

For debugging used: 
`import pdb; pdb.set_trace()`