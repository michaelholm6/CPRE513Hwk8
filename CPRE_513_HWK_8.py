from unidiff import PatchSet
import os

print(os.getcwd())
patch = PatchSet.from_filename('Homework8/output.diff', encoding='utf-8')
pass