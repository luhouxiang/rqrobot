#!C:\ProgramData\Anaconda3\envs\python3.6.5\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rqalpha==3.2.0','console_scripts','rqalpha'
__requires__ = 'rqalpha==3.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rqalpha==3.2.0', 'console_scripts', 'rqalpha')()
    )
