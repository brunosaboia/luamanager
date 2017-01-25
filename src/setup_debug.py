import os
from shutil import copyfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS_PATH = os.join(
  BASE_DIR, 'luamanager', 'luamanager', 'settings.yaml')
DEBUG_SETTINGS_PATH = os.join(
  BASE_DIR, 'luamanager', 'luamanager', 'settings_debug.yaml')

DB_PATH = os.join(BASE_DIR, 'luamanager', 'db.sqlite3')
DEBUG_DB_PATH = os.join(BASE_DIR, 'luamanager', 'db_debug.sqlite3')

if not os.path.exists(DEBUG_SETTINGS_PATH):
  copyfile(SETTINGS_PATH, DEBUG_SETTINGS_PATH)
  print('Debug settings copied')
else:
  print('Debug settings file already present, skipping...)
  
if not os.path.exists(DEBUG_DB_PATH):
  copyfile(DB_PATH, DEBUG_DB_PATH)
  print('Debug database copied')
else:
  print('Debug database file already present, skipping...)
  
print('Debug setup done.')
print('Do not forget to update settings_debug.yaml with real info.')
print('After that, you can hack away!')