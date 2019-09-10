# FPAML3.py: Runs PAML as in FPAML.py, but for the 70% Gapped Sequence ONLY
	# Non 'gap' + SEQNAME folders will give errors

##### INITIALIZATION #####

from Bio.Phylo.PAML import codeml						# Utilizing CodeML from BioPython
import glob, os

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

for folder in paml_folders:									# Loops through all current PAML folders
	file_name = folder[:-4]									# ID of the folder name
	aln_file = "%sfix.afa" % file_name						# Assigning file names
	tree_file = "%s.ph" % file_name[3:]
	curr_dir = "%s\\%s" % (os.getcwd(), folder)				# Sets current directory

	cml.alignment = "%s\\%s" % (curr_dir, aln_file)			# Setting up files for PAML analysis
	cml.tree = "%s\\%s" % (curr_dir, tree_file) 
	cml.out_file = "%s\\analysis\\output.txt" % curr_dir
	cml.working_dir = "%s\\analysis" % curr_dir
	
	cml.run(verbose = True, command = "C:\\analysis\\Phylogenetic\\paml4.8\\bin\\codeml.exe")