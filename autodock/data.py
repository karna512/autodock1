import glob # get file with certain keyword
import argparse
import os
import csv
import replace1

def get_res():
    file_list = glob.glob("res_*txt")
    result = "file,mode,affinity,rmsdlb,rmsdub"
    for file in file_list:result = result + "\n" + "\n".join([file.split(".")[0].split("res_")[1] + "," + ",".join([ii for ii in it.split(" ") if ii != ""]) for it in open(file, "r").read().split("-----\n")[-1].split("\nWriting")[0].split("\n")])  
    with open("merge.csv", 'w') as f:f.write(result)
    f.close()
    print("\n\nCollect data from file " + ", ".join(file_list) + ".\n\n")

def rename(path):
    print("\nStart renaming for file " + path)
    file_list_info = get_file_list(path)
    file_list_raw, dir_path, filenn = file_list_info[0], file_list_info[1], file_list_info[2]

    file_list = ["".join(c for c in file if c.isalpha()) for file in file_list_raw]

    for i, f1, f2 in zip(range(len(file_list)), file_list_raw, file_list):
        name1 = "{0}\\{1}.{2}".format(dir_path, f1, filenn).replace("\\", "/")
        name2 = "{0}\\{1}.{2}".format(dir_path, f2, filenn).replace("\\", "/")
        os.rename(name1, name2)
        print("{0}. rename {1}.{3} to {2}.{3}".format(i+1, f1, f2, filenn))
    print("\n")
    return [file_list, file_list_raw, dir_path, filenn]

def get_file_list(path):
    path = path.replace("/", "\\")
    file_list_raw = glob.glob(path)
    if file_list_raw == []:return [[], "", ""]
    dir_path, filenn = "\\".join(file_list_raw[0].split("\\")[:-1]) if "\\" in file_list_raw[0] else os.getcwd(), file_list_raw[0].split(".")[-1]
    file_list = [file.split(".")[-2] for file in file_list_raw]
    file_list = [file.split("\\")[-1] for file in file_list]
    
    return [file_list, dir_path, filenn]

def get_file_cross(path_set):
    path_set = path_set[:25] if len(path_set) > 25 else path_set
    path_lst_set = [get_file_list(path)[0] for path in path_set]
    result = path_lst_set[0]
    for i, path_lst in enumerate(path_lst_set[1:]):result = [it+","+it2 for it in result for it2 in path_lst]
    result = "VARIDX," + ",".join(["VAR" + chr(65+i) for i in range(len(path_set))]) + "\n" + "\n".join([str(i+1) + "," + item for i, item in enumerate(result)])
    with open("rep_cross.csv", 'w') as f:f.write(result)
    f.close()
    print(result)
    return 

if __name__ == '__main__':
    rename("*sdf")
    os.system("obabel ../autodock1/sdf_ligand/*.sdf -O ../autodock1/ligand/*.pdbqt -h -xb")
    get_file_cross(["../autodock1/receptor/*.pdbqt", "../autodock1/ligand/*.pdbqt", "../autodock1/ligand/*.pdbqt"])
    rep_gp = replace1.replace_group("rep_cross.csv", "")
    replace1.replace_file("../autodock1/receptor/config_VARA_VARB_VARC.txt", rep_gp)
    #creat rep.csv save get_file_cross
    replace1.runbat("D:/autodock1/docking.bat")
    #get_res("../autodock1/result/*.pdbqt")

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--a', type=str, default = "get_res", help='get_res')

    args = parser.parse_args()
    eval(args.a + "()")     
   # print(eval("args.a + str(5)")) see google
    #     if args.bat:runbat(args.bat)
    # if args.n >= 0:args.s = ["VARZ"] + [str(i) for i in range(args.n)]
    # if args.d:args.s = ["VARZ"] + sorted(glob.glob(args.d))
    # rep_gp = replace_group(args.S, args.s)
    # if args.i:replace_file(args.i, rep_gp)
    # if args.t:replace_txt(args.t, rep_gp)
    
    