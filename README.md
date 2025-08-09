# PyTargets
Python mini module to facilitate absolute path resolution.
## Requirements
Python 3.10+
## Usage
Create a class with a decorator to hold paths relative to .py file location (anchor) as TargetPath
```python
from targets import targets, TargetPath

@targets(__file__)
class DataDir(Targets):
    DATA = TargetPath('data')
    RAW = TargetPath('data/raw')
    PROCESSED = TargetPath('data/processed')

CLEAN_FILE = DataDir.RAW('clean.csv') # = ..../data/raw/clean.csv (absolute path)

os.makedirs(DataDir.PROCESSED) # creates .../data/processed
print(DataDir.DATA) # outputs '/data'
child_dir = DataDir.PROCESSED.split('/')[-1] # = 'processed' as TargetPath inherits from str

```
