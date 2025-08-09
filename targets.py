'''
Path resolution helper to quickly generate absolute paths.
Usage:
Create a class with a decorator to hold paths relative to .py file location (anchor) as TargetPath

from targets import targets, TargetPath

@targets(__file__) # Script's .py file location
class DataDir(Targets):
    DATA = TargetPath('data')
    RAW = TargetPath('data/raw')
    PROCESSED = TargetPath('data/processed')

CLEAN_FILE = DataDir.RAW('clean.csv') # = ..../data/raw/clean.csv (absolute path)

os.makedirs(DataDir.PROCESSED) # creates .../data/processed
print(DataDir.DATA) # outputs '/data'
child_dir = DataDir.PROCESSED.split('/')[-1] # = 'processed' as TargetPath inherits from str

'''

import os

class TargetPath(str):
    def __init__(self, relative_path : str):
        self.relative_path = relative_path
        self.anchor = './'
        self._recreate_paths()
    def _recreate_paths(self):
        self.path = os.path.abspath(os.path.join(self.anchor, self.relative_path))
    def __call__(self, filename : str = ''):
        return os.path.join(self.path, filename or '')
    def __repr__(self):
        return self.path
    def __str__(self):
        return self.path
        
def targets(anchor : str):
    if not os.path.isdir(anchor):
        anchor = os.path.dirname(anchor)
    def updater(cls):
        for v in cls.__dict__.values():
            if isinstance(v, TargetPath):
                v.anchor = anchor
                v._recreate_paths()
        return cls
    return updater