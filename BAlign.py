# MuscleAlign: Directory MUSCLE alignment
# Input: A directory of FASTA files named "#.fasta"
# Output: Within the same directory, "#.afa" aligned gene sequences and "#.ph" tree files
	
##### PROGRAM #####
	
import glob, os												# Glob = UNIX style commands
															
muscle_options = " -maxiters 8 -sv"							# Predefines options to run on all alignments
															
for fasta_file in glob.glob("*.fasta"):						# Runs the script on each file defined by glob.glob, assigned to fasta_file
	afa_file = fasta_file[:-5] + "afa"    					
	tree_file = fasta_file[:-5] + "ph"    					
	command = "muscle -in %s -out %s -tree2 %s %s" % (fasta_file, afa_file, tree_file, muscle_options)
															# Creates the appropriate command for MUSCLE
	os.system(command) 										# Running of the string 'command'