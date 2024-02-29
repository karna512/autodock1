import glob # get file with certain keyword
import argparse

def get_res():
    file_list = glob.glob("res_*txt")
    result = "file,mode,affinity,rmsdlb,rmsdub"
    for file in file_list:result = result + "\n" + "\n".join([file.split(".")[0].split("res_")[1] + "," + ",".join([ii for ii in it.split(" ") if ii != ""]) for it in open(file, "r").read().split("-----\n")[-1].split("\nWriting")[0].split("\n")])  
    with open("merge.csv", 'w') as f:f.write(result)
    f.close()
    print("\n\nCollect data from file " + ", ".join(file_list) + ".\n\n")
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--a', type=str, default = "get_res", help='get_res')

    args = parser.parse_args()
    eval(args.a + "()")     
   # print(eval("args.a + str(5)")) see google