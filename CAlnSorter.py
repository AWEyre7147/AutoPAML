# AlnSorter: Directory-wise sorting of data within MUSCLE aligned files
# Input:  Directory of #.afa files
# Output:  Directory of #sort.afa files

##### FUNCTIONS #####

def sorter(afa_file, output):
	file_text = file(afa_file).readlines()					# Breaks lines into a vector
	data = ''
	i = 0
	
	for line in file_text:									# Loops through all lines in file_text
			line = line.strip()
			if line.startswith('>'):						# Checks if the line is a header
				if i < 2:
					data = "%s\n" % line
				else:
					data = "%s\n%s\n" % (data,line)
				i = i + 1
			else:
				data = "%s%s" % (data,line)
				i = i + 1
			
	output.write(data)
									
	
##### PROGRAM #####

import glob

for afa_file in glob.glob('*.afa'):							# Input file defined by UNIX module.  glob.glob like file()
	outsort_name = afa_file[:-4] + 'sort.afa'				# Sorter output file name
	outsort = file('%s' % outsort_name, 'wt')				# Sorter output file, seqcheck input
		
	sorter(afa_file, outsort)

