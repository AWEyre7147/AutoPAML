# AutoPAML

These are a series of scripts that I used to run CodeML on large gene datasets for two publications, however these are setup for one of the publications.  The data used were a directory of FASTA files containing transcript orthologs between Magnaporthe Oryzae, the rice blast fungus, and two of its closest sequenced ancestors.

CodeML is a maximum likelihood algorithm for determining (1) the probability that a cluster of aligned DNA sequences are undergoing directional selection, and if so, (2) whether the directional seletion is diversifying (more nonsynonymous mutations) or purifying (more synonymous mutations). 

Note:  These codes were developed at the very beginning of my coding career, so they are not the best formatted/designed - be gentle!

## Getting Started

PAML can be found at http://abacus.gene.ucl.ac.uk/software/paml.html

I would recommend reading the publication(s) associated with the PAML and CodeML, and play with a few toy datasets and the GUI.

### Prerequisites

Python 2.7
PAML commandline
MUSCLE (sequence alignment)

### Installing

Simply download the scripts and modify as needed, they are annotated for readability.

## Description of Scripts:

ASeqSort:     C

BAlign:       O

CAlnSorter:   M

CGapExp:      I

DNucCheck:    N

EDirSorter:   G

EDirSorter2:  

FPAML:        S

FPAML2:       O

FPAML3:       O

GPreResult:   N

GResult:      

HPreStat:     

HStat:        

## Acknowledgments

* Yang, Z. 1997. PAML: a program package for phylogenetic analysis by maximum likelihood. Computer Applications in BioSciences 13:555-556.
* Yang, Z. 2007. PAML 4: a program package for phylogenetic analysis by maximum likelihood. Molecular Biology and Evolution 24: 1586-1591
* Fungal Genomics Laboratory and Collaborators
