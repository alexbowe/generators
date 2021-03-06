#!/usr/bin/env python

from Generator import Generator

class NameGenerator(Generator):
    "Name Generator"
    # Default Files Extracted From:
    # http://www.census.gov/genealogy/www/data/1990surnames/names_files.html
    filenames = {
                    'lastname' : 'data/lastnames.txt',
                    'femalename' : 'data/f_firstnames.txt',
                    'malename' : 'data/m_firstnames.txt'
                }
                
    def __init__(self):
        Generator.__init__(self, NameGenerator.filenames)

if __name__ == '__main__':
    ngen = NameGenerator()
    assert(ngen.lastname())
    assert(ngen.femalename())
    assert(ngen.malename())
    print ngen.malename()