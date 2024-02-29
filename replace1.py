import argparse
import glob
import os
from subprocess import Popen

def replace_group(csv_group, cmd_group):
    if csv_group == "":return [[it] for it in cmd_group]
    return [it.split(",") for it in open(csv_group, 'r').read().split("\n") if it != ""]

def replace_file(file_name, replist):
    file = open(file_name, 'r').read()
    for i, rep in enumerate(replist[1:]):                                 
        file_new, file_name_new = file, file_name
        for j, rep2 in enumerate(replist[0]):file_new = file_new.replace(rep2, rep[j])
        for j, rep2 in enumerate(replist[0]):file_name_new = file_name_new.replace(rep2, rep[j])
        with open(file_name_new, 'w') as f:f.write(file_new)
        f.close()
    print("\nTotally create " + str(len(replist)-1) + " files.\n")

def replace_txt(cmd, replist):
    print("\n\n")
    for i, rep in enumerate(replist[1:]):
        cmd_new = cmd
        for j, rep2 in enumerate(replist[0]):cmd_new = cmd_new.replace(rep2, rep[j])
        print(cmd_new)
    print("\n\n")
    exit() 
    # for cmd commend, if we use data_analysis, don't conduct this code.

def runbat(path):

    path = path.replace("\A"[0], "/A"[0]).replace("//", "/")
    cwd = "/".join(path.split("/")[:-1]) if "/" in path else os.getcwd()
    p = Popen(path, cwd=cwd)
    stdout, stderr = p.communicate()
    print("Run " + path + " successfully!")
    exit() 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--i', type=str, default = "", help='get config file')    # get config file 
    parser.add_argument('-t', '--t', type=str, default = "", help='get cmd')            # get cmd str
    parser.add_argument('-S', '--S', type=str, default = "", help='replace thru .csv')  # start from my csv
    parser.add_argument('-s', '--s', nargs='+', help='replace by cmd')                  # get it strait to rename/creat config file
    parser.add_argument('-d', '--d', type=str, default = "", help='all files')          # call all file
    parser.add_argument('-n', '--n', type=int, default = -1, help='number')
    parser.add_argument('-bat', '--bat', type=str, default = "", help='run .bat')
    args = parser.parse_args()

    if args.bat:runbat(args.bat)
    if args.n >= 0:args.s = ["VARZ"] + [str(i) for i in range(args.n)]
    if args.d:args.s = ["VARZ"] + sorted(glob.glob(args.d))
    rep_gp = replace_group(args.S, args.s)
    if args.i:replace_file(args.i, rep_gp)
    if args.t:replace_txt(args.t, rep_gp)
    


#python D:\autodock\replace.py -S D:\autodock\rep.csv -s VARB -i config_VARB.txt
#python D:\autodock\replace.py -S D:\autodock\rep.csv -t "D:\autodock\vina --config config_VARB.txt > res_VARB.txt"
#python D:\autodock\replace.py -S D:\autodock\rep.csv -t "D:\autodock\vina --config VARZ -d tmp/*txt"
#python .\replace.py -bat C:/Users\\\\Goat\Downloads/vina_sample/zz.bat 

