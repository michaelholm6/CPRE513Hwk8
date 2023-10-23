from unidiff import PatchSet
import os
import subprocess
import numpy as np
import math
import shutil

step_number = 1

def detect_bug(original_source_code, patch_indeces, r, patch_collection, config_number):

    global step_number
    
    print('Step: ' + str(step_number), end=' ')
    print('c_' + str(config_number) + ': ', end='')

    if os.path.isfile('patch_file.patch'):
        os.remove('patch_file.patch')

    if os.path.isfile('file1v1.java'):
        os.remove('file1v1.java')
       
    shutil.copy(original_source_code, 'file1v1.java')
    
    patch_indeces = sorted(patch_indeces + r)
    
    print(patch_indeces, end=' ')

    for patch_index in patch_indeces:
            patch_collection[patch_index]
            patch = open('patch_file.patch', "a")
            patch.write(str(patch_collection[patch_index]))
            patch.close()
            

    os.system('patch file1v1.java patch_file.patch > /dev/null')

    os.system('javac file1v1.java')
    
    output = subprocess.Popen(["java", "file1v1", "5", "0", "division"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE).communicate()[1]
    
    if "/ by zero" in str(output):
        print('Fail')
        step_number += 1
        return True
    
    else:
        print('Pass')
        step_number += 1
        return False
        
def delta_debugging(c, r, original_source_code, patch_collection):
    global found_bug_list
    c1 = (0, math.floor(len(c)/2))
    c1 = c[c1[0]:c1[-1]]
    c2 = (math.floor(len(c)/2), len(c))
    c2 = c[c2[0]:c2[-1]]
    
    if len(c) == 1:
        found_bug_list.append(c)
        return
        
    elif detect_bug(original_source_code, c1, r, patch_collection, 1):
        delta_debugging(c1, r, original_source_code, patch_collection)
        
    elif detect_bug(original_source_code, c2, r, patch_collection, 2):
        delta_debugging(c2, r, original_source_code, patch_collection)
        
    else:
        c2_new = c2 + r
        delta_debugging(c1, c2_new, original_source_code, patch_collection)
        c1_new = c1 + r
        delta_debugging(c2, c1_new, original_source_code, patch_collection)
        
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

print("Changes that occured:")

for patch_hunk in patch[0]:
    print(str(patch_hunk).partition('\n')[0])
    
print('Number of changes is ' + str(len(patch[0])))
    
patch_index_list = [i for i in range(len(patch[0]))]
    
found_bug_list = []

delta_debugging(patch_index_list, [], original_file, patch[0])

print('Changes where bugs occured:' + str(found_bug_list[0]))
    
os.chdir('..')
    
shutil.rmtree(folder_name)
    
        
    
    
    
    
    

