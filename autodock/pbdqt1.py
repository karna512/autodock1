import os
import re

def rename_pdbqt_files(directory):
    for file in os.listdir(directory):
        if file.endswith(".pdbqt"):
            new_name = re.sub(r'[^a-zA-Z\.]', '', file)
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

if __name__ == "__main__":
    directory_path = r'D:\autodock'
    rename_pdbqt_files(directory_path)
    print("PDBQT files renamed successfully.")
