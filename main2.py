import sys
import os
import subprocess

def fun(text):
        print(" SEARCHING ACTION \n")

        # build keywords list, we'll use this to search
        keywords = text
        keywords = text.lower().split(' ')
        print('Searching with keywords:  ' + str(keywords))


        fname = dir_path + '/search_keywords.txt'
        with open(fname, 'w') as f:
                 f.write(str(keywords))


        shell_script = dir_path + '/cleanup.sh'
        returncode = subprocess.call(['sh', shell_script])
        if not returncode == 0:
                print('\n\n\t\t:: ERROR --> __CLEANUP__ Script Failed')
        # run the query shell script
        shell_script = dir_path + '/query_run.sh'
        returncode = subprocess.call(['sh', shell_script])
        if not returncode == 0:
                print('\n\n\t\tERROR --> __Query MapReduce__ Job Failed')
