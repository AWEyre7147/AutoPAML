# DirSorter2: Organizes the files created for 70% Gap + Aligned by GapExp.py
	
##### PROGRAM #####

import glob, os, shutil

for main_file in glob.glob('*fix.afa'):							# Input file defined by UNIX module.
	if "gap" in main_file:
		fasta_file = main_file[3:-7] + ".fasta"
		tree_file = main_file[3:-7] + ".ph"
	else:	
		fasta_file = main_file[:-7] + ".fasta"
		tree_file = main_file[:-7] + ".ph"
	
	move_files = [main_file, fasta_file, tree_file]
	curr_dir = os.path.dirname(os.path.realpath(main_file))		# Assigns the directory name to curr_dir
	os.makedirs(main_file[:-7] + "PAML/analysis")				# Creates the new folders
	dest_dir = curr_dir + "\\" + main_file[:-7]	+ "PAML"		# Assigns the new folder to dest_dir
	
	for file in move_files:	
		if "gap" in main_file:
			shutil.copyfile("%s\\%s" % (curr_dir, file), "%s\\%s" % (dest_dir, file))
		else:
			os.remove("%s.txt" % main_file[:-7])									
			os.remove("%ssort.afa" % main_file[:-7])
			os.remove("%s.afa" % main_file[:-7])
			os.rename("%s\\%s" % (curr_dir, file), "%s\\%s" % (dest_dir, file))
