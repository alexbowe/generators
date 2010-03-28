#!/usr/bin/env python

from CachedFile import CachedFile

def add_method(obj, f, fname):
    """Adds the instance method from function f to the object obj,
    callable by fname (i.e. obj.fname())"""
    from new import instancemethod
    obj.__dict__[fname] = instancemethod(f, obj, obj.__class__)

class Generator:
    "Generator for random data provided by a dictionary of files"
    # This will contain each file's contents if/when required -
    # Files are opened lazily as we don't always want to open them
    files = { }
    
    def __init__(self, filenames_dict):
        """Constructs a Generator with methods (named after each key) for
        randomly selecting a line from each file in the dictionary"""
        for key in filenames_dict:
            self.files[key] = CachedFile(filenames_dict[key])
            add_method(self, self.make_func(key), key)

    def make_func(self, key):
        """Makes a function to wrap get_random to a specific key"""
        def f(self):
            return self.get_random(key)
        return f

    def get_random(self, key):
        """Returns a randomly selected item from the appropriate file as 
        specified by key"""
        contents = self.files[key].readlines()
        from random import choice
        return choice(contents).strip()
