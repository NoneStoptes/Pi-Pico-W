from builtins import exec
from morsecode import morse
with open('morsecode.py', 'r') as f:
    morsecode_content = f.read()
exec(morsecode_content)
morse()