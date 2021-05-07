import sys
import os
import subprocess

def fun(text):
	print(" SEARCHING ACTION \n")

	# build keywords list, we'll use this to search
	keywords = text
	#keywords = text.lower().split(' ')
	print('Searching with keywords:  ' + str(keywords))

        # save keywords list to a file, so the query mapper/reducer can both
        # read same list of keywords, and inform their search effort
	dir_path = os.path.dirname(os.path.realpath(__file__))
	fname = dir_path + '/search_keywords.txt'
	with open(fname, 'w') as f:
		 f.write(str(keywords))
		 

	"""
	# run the preprocessing shell script
	shell_script = dir_path + '/preprocess.sh'
	returncode = subprocess.call(['sh', shell_script])
	if not returncode == -1:
		print('\n\n\t\tERROR --> __Preprocessing__ Failed')
        
	
	# run the inverted index shell script
	shell_script = dir_path + '/inverted_index_run.sh'
	returncode = subprocess.call(['sh', shell_script])
	if not returncode == 0:
		print('\n\n\t\tERROR --> __Inverted Index__ MapReduce Job Failed')
	"""
	print(" CLEANUP \n")
	# Remove files from last run, so user can re-run the script
	shell_script = dir_path + '/cleanup.sh'
	returncode = subprocess.call(['sh', shell_script])
	if not returncode == 0:
		print('\n\n\t\t:: ERROR --> __CLEANUP__ Script Failed. You may need to delete Hadoop output directories manually.')
	# run the query shell script
	shell_script = dir_path + '/query_run.sh'
	returncode = subprocess.call(['sh', shell_script])
	if not returncode == 0:
		print('\n\n\t\tERROR --> __Query MapReduce__ Job Failed')
	
fun(sys.argv)


