# SequenceRename: Directory FASTA reformatting
# Input:  Directory of #.txt files in FASTA format
# Output:  #.fasta files in the same directory with truncated headers for use in PAML
	
##### PROGRAM #####

import glob													# UNIX command module

for txt_file in glob.glob('*.txt'):							
	fasta_name = txt_file[:-3] + "fasta"					
	output = file('%s' %fasta_name, 'wt')					
	file_text = file(txt_file).readlines()					
	
	for line in file_text:									
		line = line.strip()									
		if line.startswith('>'):							
			header = line.split()							
			line = header[0]								
		output.write("%s\n" % line)							 							