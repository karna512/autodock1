import os
import csv

def list_sdf_files(directory):
    sdf_files = []
    for file in os.listdir(directory):
        if file.endswith(".sdf"):
            file_name = os.path.splitext(file)[0]
            file_name = ''.join(c for c in file_name if c.isalpha())
            sdf_files.append(file_name)
    return sdf_files

def write_to_csv(file_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name"])
        for file in file_list:
            writer.writerow([file])

if __name__ == "__main__":
    directory_path = r'D:\autodock'
    output_csv_file = 'sdf_files.csv'

    sdf_files = list_sdf_files(directory_path)
    write_to_csv(sdf_files, output_csv_file)

    print(f"CSV file with SDF file names created: {output_csv_file}")
