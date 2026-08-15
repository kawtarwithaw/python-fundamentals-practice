

# replace with your own folder paths
source_folder = "C:\\..."  
destination_folder = "C:\\..."

import os
import shutil
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("works")
files = os.listdir(source_folder)
for filename in files:
     if filename.endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print("Moved:", filename)
