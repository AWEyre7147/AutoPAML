# NucCheck: Directory scanning of aligned, AlnSorter organized files
# Input:  Directory of #sort.afa files
# Output:  Directory of #fix.afa files

##### FUNCTIONS #####

def seqcheck(seq_file, output):
	file_text = file(seq_file).readlines()
	
	for line in file_text:									# Loops through all lines in file_text
			if line.startswith('>'):						# Checks if the line is a header
				line = line									# Maintains header identity
			else: 											 
				line = line.strip()							# Strips \n characters
				if len(line)%3 != 0:						# Checks if NOT divisible by 3
					line = line + '-' * (3 - len(line)%3) + '\n'
				else:											# Adds terminal gap characters to achieve divisibility, readd \n
					line = line + '\n'						# Nothing done otherwise, readd \n
			output.write("%s" % line)						# Writes line
	
##### PROGRAM #####

import glob

for sort_file in glob.glob('*sort.afa'):					# Input file defined by UNIX module.  glob.glob like file()
	outseq_name = sort_file[:-8] + 'fix.afa'				# Seqcheck output file name
	outseq = file('%s' % outseq_name, 'wt')					# Seqcheck output file
	
	seqcheck(sort_file, outseq)								# Runs function with proper inputs

