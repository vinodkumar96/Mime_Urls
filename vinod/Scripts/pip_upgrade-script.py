#!C:\PyCharm\PycharmProjects\new_projects\Mime_Urls\vinod\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip-upgrade==0.0.6','console_scripts','pip_upgrade'
__requires__ = 'pip-upgrade==0.0.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip-upgrade==0.0.6', 'console_scripts', 'pip_upgrade')()
    )
