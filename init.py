### import ###
import os
import shutil
import subprocess
import urllib.request
import zipfile

### CodeIgniter ###
CODE_IGNITER_VER = "3.1.10"

# download
url = "https://github.com/bcit-ci/CodeIgniter/archive/" + CODE_IGNITER_VER + ".zip"
save_name = "CodeIgniter.zip"
urllib.request.urlretrieve(url, save_name)

# unzip
with zipfile.ZipFile("./CodeIgniter.zip") as existing_zip:
    existing_zip.extractall("./")

# mkdir
if not os.path.exists("./html"):
    os.makedirs("./html")
if not os.path.exists("./mysql/data"):
    os.makedirs("./mysql/data")
if not os.path.exists("./phpmyadmin/sessions"):
    os.makedirs("./phpmyadmin/sessions")

# copy
source_dir = "./CodeIgniter-" + CODE_IGNITER_VER
target_dir = "./html"
shutil.copy(source_dir + "/index.php", target_dir + "/index.php")
if not os.path.exists(target_dir + "/application"):
    shutil.copytree(source_dir + "/application", target_dir + "/application")
if not os.path.exists(target_dir + "/system"):
    shutil.copytree(source_dir + "/system", target_dir + "/system")

# delete
os.remove("./CodeIgniter.zip")
shutil.rmtree(source_dir)

# setting
shutil.copy("./php/.htaccess", "./html/.htaccess")
shutil.copy("./php/database.php", "./html/application/config/database.php")
shutil.copy("./php/config.php", "./html/application/config/config.php")
