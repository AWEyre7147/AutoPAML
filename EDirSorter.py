# DirSorter: Organizes the files created by earlier scripts for PAML
# Input:  Directory of files
# Output:  Files sorted into new directories
	
##### PROGRAM #####

import glob, os

for main_file in glob.glob('*fix.afa'):							# Input file defined by UNIX module.
	del1_name = main_file[:-7] + ".txt"							# Variable names for files
	del2_name = main_file[:-7] + "sort.afa"
	del3_name = main_file[:-7] + ".afa"
	fasta_name = main_file[:-7] + ".fasta"
	tree_name = main_file[:-7] + ".ph"
	move_files = [main_file, fasta_name, tree_name]
	
	os.remove(del1_name)										# Removes unneeded files
	os.remove(del2_name)
	os.remove(del3_name)
	
	curr_dir = os.path.dirname(os.path.realpath(main_file))		# Assigns the directory name to curr_dir
	make_dir = main_file[:-7] + "PAML/analysis"					# Assigns the new folders names to make_dir
	os.makedirs(make_dir)										# Creates the new folders
	dest_dir = curr_dir + "\\" + main_file[:-7]	+ "PAML"		# Assigns the new folder to dest_dir
	
	for file in move_files:										# Loops through all files needing to be moved
		from_folder = curr_dir + "\\" + file					# Variable names for destinations
		to_folder = dest_dir + "\\" + file
		os.rename(from_folder, to_folder)						# Moving files
	
	

