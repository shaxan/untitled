#!C:\Users\SALAVAT\PycharmProjects\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hexlet==0.6.3','console_scripts','hexlet'
__requires__ = 'hexlet==0.6.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hexlet==0.6.3', 'console_scripts', 'hexlet')()
    )
