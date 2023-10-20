from unidiff import PatchSet
import os
from diff_match_patch import diff_match_patch
import subprocess
import numpy as np

print(os.getcwd())
patch = PatchSet.from_filename('Homework8/output.diff', encoding='utf-8')
chunk_list = []
original_file = input('Path to original file source code\n')
buggy_file = input('Path to buggy file source code\n')
original_executable = input('Path to original executable\n')
buggy_file = buggy_file.strip()
original_file = original_file.strip()
original_file = open(original_file, 'r')
original_file = original_file.read()
buggy_file = open(buggy_file, 'r')
buggy_file = buggy_file.read()
patch_array = np.asarray(patch[0])

diff_file = ''

for i, chunk in enumerate(patch_array[[0, -1]]): 
    diff_file = diff_file + str(chunk)
    
dmp = diff_match_patch()
dmp.Match_Threshold = 1
dmp.Patch_DeleteThreshold = 1
patch = dmp.patch_fromText(diff_file)

patched_file = original_file

patched_file, _ = dmp.patch_apply(patch, original_file)

if not os.path.exists('temp_folder'):
    os.mkdir('temp_folder')

patched_file_opened = open('temp_folder/java1v2.java', 'w')
patched_file_opened.write(patched_file)
patched_file_opened.close()
proc = os.system('javac temp_folder/java1v2.java')

pass
