# FPAML.py: Runs PAML on a directory of folders containing necessry files for each run
# Input:  Directory of folders with associated files
# Output:  Just the PAML analyses to the 'analysis' folder

##### INITIALIZATION #####

from Bio.Phylo.PAML import codeml						# Utilizing CodeML from BioPython
import glob

cml = codeml.Codeml()									# Defines CodeML variable
	
cml.set_options(verbose = 0)							# Set CodeML Options for all analyses
cml.set_options(CodonFreq = 2)
cml.set_options(cleandata = 0)
cml.set_options(fix_blength = 0)
cml.set_options(NSsites=[0, 1, 2, 7, 8])
cml.set_options(fix_omega = 0)
cml.set_options(clock = 1)
cml.set_options(ncatG = 2)
cml.set_options(runmode = 0)
cml.set_options(fix_kappa = 0)
cml.set_options(fix_alpha = 1)
cml.set_options(Small_Diff = 5e-7)
cml.set_options(method = 1)
cml.set_options(Malpha = 0)
cml.set_options(aaDist = 0)
cml.set_options(RateAncestor = 0)
cml.set_options(icode = 0)
cml.set_options(alpha = 0.0)
cml.set_options(seqtype = 1)
cml.set_options(omega = 0.4)
cml.set_options(getSE = 0)
cml.set_options(noisy = 3)
cml.set_options(Mgene = 0)
cml.set_options(kappa = 2)
cml.set_options(model = 0)
cml.set_options(ndata = 1)	

##### PROGRAM #####				

paml_folders = glob.glob('*PAML')							# Creation of a sorted number list the length of the files in the directory
paml_folder = range(len(paml_folders))						# Creates a list the length of the number of folders
paml_folder = [x+1 for x in paml_folder]					# Shifts all values up by 1 for naming reasons

for folder in paml_folder:									# Loops through all current PAML folders
	folder_name = ('%s' + 'PAML') % folder					# ID of the folder name
	curr_dir = "C:\\analysis\\" + folder_name				# Sets current directory
	curr_test = folder_name[:-4]							# Assigns test number to a variable
	aln_file = curr_test + 'fix.afa'						# Assigning file names
	tree_file = curr_test + '.ph'
	
	cml.alignment = curr_dir + "\\" + aln_file				# Setting up files for PAML analysis
	cml.tree = curr_dir + "\\" + tree_file 
	cml.out_file = curr_dir + "\\analysis\\output.txt"
	cml.working_dir = curr_dir + "\\analysis"
	
	cml.run(verbose = True, command = "C:\\analysis\\Phylogenetic\\paml4.8\\bin\\codeml.exe")
															
	results = codeml.read(cml.out_file)