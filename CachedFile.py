#!/usr/bin/env python

import unittest

class CachedFile:
    """Lazily opens a file and stores a readlines() call intermediately
    after it is called, for use in future calls readlines() calls"""
    
    filename = ''
    filecontents = None
    
    def __init__(self, filename):
        """Constructs a new CachedFile which will attempt to open the 
        specified file for reading. File is opened lazily, so if the file 
        doesn't exist, it won't be detected right away."""
        self.filename = filename
        
    def readlines(self):
        """Reads all the lines of a file and returns them in an array. If the 
        lines were read previously, it'll return a cached array. Raises IOError
        if the file does not exist."""
        if self.filecontents is None:
            # Temporarily Open File and read all lines
            with open(self.filename, 'r') as f:
                self.filecontents = f.readlines()
        
        return self.filecontents

class TestCachedFile(unittest.TestCase):
    """Unit test for CachedFile"""
    
    def test_readlines_nonexistent(self):
        """Tests for IOError for a file that doesn't exist"""
        fakefilename = gen_fake_filename()
        cf = CachedFile(fakefilename)
        self.assertRaises(IOError, cf.readlines)
        
    def test_readlines_exists(self):
        """Tests for the absence of an IOError for a file that does exist"""
        import inspect
        # the file that this code is in must exist...
        sourcefile = inspect.getsourcefile(TestCachedFile)
        # if an exception is raised this will fail
        cf = CachedFile(sourcefile)
    
def gen_fake_filename():
    """Generates a filename that doesn't exist"""
    filename = 'notarealfile'
    import os
    # if the file exists, keep adding to it
    while os.path.isfile(filename):
        filename += 'x'

    return filename

if __name__ == '__main__':
    unittest.main()
