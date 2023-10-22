from unidiff import PatchSet
import os
import subprocess
import numpy as np
import math
import shutil

def detect_bug(original_source_code, patch_indeces, patch_collection):

    patch_indeces = [0,1,2,3,4,5,6,7,8,9,10]

    if os.path.isfile('patch_file.patch'):
        os.remove('patch_file.patch')

    if os.path.isfile('file1v1.java'):
        os.remove('file1v1.java')
       
    shutil.copy(original_source_code, 'file1v1.java')

    for patch_index in patch_indeces:
            patch_collection[patch_index]
            patch = open('patch_file.patch', "a")
            patch.write(str(patch_collection[patch_index]))

    os.system('patch file1v1.java patch_file.patch')

    os.system('javac file1v1.java')
    
    output = subprocess.Popen(["java", "file1v1", "5", "0", "division"], stdout=subprocess.PIPE).communicate()[0]
    
    if "b''" == str(output):
        return True
    
    else:
        return False
        
def delta_debugging(c, r, original_source_code, patch_collection):
    c1 = (0, math.floor(len(c)/2))
    c1 = c[c1[0]:c1[-1]]
    c2 = (math.floor(len(c)/2), len(c))
    c2 = c[c2[0]:c2[-1]]
    
    if len(c) == 1:
        print(found_bug_list.append(c))
        
    detect_bug(original_source_code, c1, patch_collection)
    
    return

cwd = os.getcwd()
chunk_list = []
original_file = input('Absolute path to original file source code\n')
buggy_file = input('Absolute path to buggy file source code\n')
folder_name = input('Give a new folder name to store temporary data in (This folder will be deleted at the end of the process)\n')

if os.path.exists(folder_name):
    raise Exception('Provide a folder name that doesn\'t already exist')

os.mkdir(folder_name)

os.chdir(os.path.join(cwd, folder_name))

os.system('diff -U 0 ' + repr(original_file) + ' ' + repr(buggy_file) + ' > output.diff')
patch = PatchSet.from_filename('output.diff', encoding='utf-8')
    
patch_index_list = [i for i in range(len(patch[0]))]
    
found_bug_list = []

delta_debugging(patch_index_list, [], original_file, patch[0])
    
    
    
        
    
    
    
    
    

