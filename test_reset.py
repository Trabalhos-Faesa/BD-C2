import sys
sys.path.insert(0, 'src')

from utils.db import exec_script

result = exec_script('management/reset_db.sql')
print(result)
