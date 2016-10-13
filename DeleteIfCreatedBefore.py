
# Usage:  DeleteIfCreatedBefore.py <File1> <File2>
#
# Compare creation times of <File1> and <File2>.
# Delete <File1> if its creation time is earlier.


import sys, os.path

def DeleteIfCreatedBefore(file1, file2):
    '''Delete file1 if it was created before file2.'''
    if os.path.exists(file1) and os.path.exists(file2):
        if os.path.getctime(file1) < os.path.getctime(file2):
            os.remove(file1)

try:
    assert len(sys.argv) == 3, 'USAGE:  DeleteIfCreatedBefore.py <File1> <File2>'
    DeleteIfCreatedBefore(sys.argv[1], sys.argv[2])
except BaseException, e:
    print e


# This code runs correctly on Windows systems.
#
# os.path.getctime(path) returns the system's ctime which, on some systems (like Windows),
# is the creation time for path, and on others (like Unix) is the time of the last change.
# The return value is the number of seconds since the epoch.  Raises os.error if the file
# does not exist or is inaccessible.
