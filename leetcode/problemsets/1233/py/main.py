# Solution to leetcode problem 1233
#
# Start  10:42
# Finish 11:19
#
# Folders are lists of strings (separated by "/")
# A folder B is a subfolder of folder A if 
# the list form of B is a prefix of the list form of A.

from typing import List

def a_is_prefix_of_b(a, b):
    if a is None or b is None:
        return False
    if len(a) > len(b):
        return False
    return not any([x != y for (x, y) in zip(a, b)])
    #return all([x == y for (x, y) in zip(a, b)])
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        no_prefix_folders = []
        folder.sort()
        parsed_folder = [x.split("/") for x in folder]
        prev_prefix = None
        for (i_f, f) in enumerate(parsed_folder):
            if a_is_prefix_of_b(prev_prefix, f):
                continue
            else:
                prev_prefix = f
                no_prefix_folders.append(folder[i_f])
        return no_prefix_folders
    
class SolutionOneLine:
    def xremoveSubfolders(self, a: List[str]) -> List[str]:
        return (q:='_') and [q:=v for v in sorted(a) if v.find(q+'/')]
    def removeSubfolders(self, a: List[str]) -> List[str]:
        q= '_'
        retval = []
        for v in sorted(a):
            print(f"{q=}, {v=}, {v.find(q+'/')=}")
            if v.find(q+'/'):
                print(f"appending {v=}")
                q = v
                retval.append(v)
            else:
                print(f"skipping {v=}")
        return retval
