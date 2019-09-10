# AutoPAML (2016)

These are a series of scripts that were used to run CodeML on large gene datasets for two publications.  The data used were a directory of FASTA files containing transcript orthologs between Magnaporthe Oryzae, the rice blast fungus, and two of its closest sequenced ancestors.  

CodeML is a maximum likelihood algorithm for determining (1) the probability that a cluster of aligned DNA sequences are undergoing directional selection, and if so, (2) whether the directional seletion is diversifying (more nonsynonymous mutations) or purifying (more synonymous mutations). 

Note 1:  These codes were written while I first learning to code and are therefore lacking and very sloppy (sorry!).  If there are any questions related to the code, please feel free to contact me.

Note 2:  These codes were not formatted to be used by all users.  The main compatibility issues lie in accessing the file names (easy) and ensuring the file contents are consistent with the code (more difficult - not much of an issue after alignment)

### Prerequisites

Python 2.7
PAML commandline
MUSCLE (sequence alignment)

### Installation 

Extract files to a directory.

## Description of Scripts

ASeqSort:     .txt to .fasta file converter

BAlign:       MUSCLE alignment of .fasta files

CAlnSorter:   Sorts data within the MUSCLE (.afa) output files 

CGapExp:      Removes columns in the alignment if they have a certain % of gaps (experimental - this designed to answer questions relating to gaps)
                  - Note: This value is set to 70%, which was selected based upon the number of alignments in each file

DNucCheck:    Checks if the alignments are divisible by 3 (a requirement for PAML) and corrects with terminal gaps

EDirSorter:   Deletes intermediate files, creates new directories, sorts files

EDirSorter2:  Same as above, but used if the gap removal tool was used

FPAML:        Runs PAML for each file

FPAML2:       Runs PAML, but with cleandata function utilized

FPAML3:       Runs PAML for the files generated if the gap removal tool was used

GPreResult:   Reads PAML output and generates a directory of the output values

GResult:      Conglomerates PAML results into a single file

HPreStat:     Obtains values from result file for statistical analysis

HStat:        Creates a final file containing all of the results for downstream analysis

## Acknowledgments

* Yang, Z. 1997. PAML: a program package for phylogenetic analysis by maximum likelihood. Computer Applications in BioSciences 13:555-556.
* Yang, Z. 2007. PAML 4: a program package for phylogenetic analysis by maximum likelihood. Molecular Biology and Evolution 24: 1586-1591
* Fungal Genomics Laboratory and Collaborators
