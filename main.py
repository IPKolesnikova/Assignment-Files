__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile
from zipfile import ZipFile

path = os.getcwd() + "\\cache"
zip_file_path=os.getcwd() + "\\data.zip"


#1
def clean_cache():
    if os.path.isdir('cache'):
        shutil.rmtree(path)
        os.mkdir(path)
    else:    
        os.mkdir(path)
clean_cache()
#2
def cache_zip(zip_file_path, path):
    clean_cache()
    with zipfile.ZipFile(zip_file_path, 'r') as data:
        data.extractall(path)

cache_zip(zip_file_path, path)        

#3
def cached_files():
    absolute_path = [os.path.join(path, file) for file in os.listdir(path)]
    return absolute_path

#4
def find_password(cached_files):
    for f in cached_files:
        search = open(f, "r")
        for line in search:
            if "password" in line:
                password = line[line.find(" ") + 1 :-1]
                return password
