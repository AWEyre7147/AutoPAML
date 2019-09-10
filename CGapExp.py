# GapExp.py
# Input:
# Output:

##### FUNCTIONS #####

def head_seq(file_text):
	i = 0
	header = list()
	sequence = list()
	
	for line in file_text:											# Header/Sequence Variable Sorter
		line = line.strip()
		if i%2 == 0:
			header.append(line)
			i = i + 1
		else:
			sequence.append(line)
			i = i + 1
	return header, sequence

def gap_builder(sequence):
	nuc_count = 0
	print len(sequence[0])
	
	while nuc_count < len(sequence[0]):								# Loop that deletes sequence column if it's >70% Gaps
		gap_sum = 0
		col_sum = float(len(sequence))
		
		for seq in sequence:										# Sequence Gap Counter							 
			if seq[nuc_count] == '-':
				gap_sum = gap_sum + 1
			else:
				gap_sum = gap_sum
		
		if gap_sum / col_sum > 0.7:								# 70% Gap Checker
			i = 0
			for seq in sequence:
				new_seq = list(seq)
				new_seq[nuc_count] = ''
				new_seq = ''.join(new_seq)
				sequence[i] = new_seq
				i = i + 1
			nuc_count = nuc_count
		else:
			nuc_count = nuc_count + 1
	
	print len(sequence[0])
	return sequence

			
##### PROGRAM #####

import glob

for sort_file in glob.glob('*sort.afa'):					
	seq70_name = 'gap' + sort_file[:-8] + 'sort.afa'	
	out70 = file('%s' % seq70_name, 'wt')
	file_text = file(sort_file).readlines()
	
	header, sequence = head_seq(file_text)
	sequence1 = gap_builder(sequence)
	
	i = 0
	for title in header:
		data = "%s\n%s\n" % (title, sequence1[i])
		out70.write("%s" % data)
		i = i + 1