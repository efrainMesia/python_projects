import os 
import shutil
import re
import argparse

def check_path(path):
    if(os.path.exists(path)):
        #print("File exist")
        return True
    else:
        #print("File does not exist")
        return False

def delete_file(path):
    if(check_path(path)):
        print("Removing",path)
        if(os.path.isdir(path)):
            shutil.rmtree(path,ignore_errors=True)
        else:
            os.remove(path)
        return True
    else:
        return True


def _copy_file(src_path,dst_path):
    if(check_path(src_path) and delete_file(dst_path)):
        create_dir(dst_path)
        if(shutil.copyfile(src_path,dst_path)):
            print("File copied succesfully")
            return True
    else:
        print("Source path/file does not exist")
        return False

def create_dir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.mkdir(dir)

def _copy_dir(src_path,dst_path):
    if(check_path(src_path) and delete_file(dst_path)):
        create_dir(dst_path)
        if(shutil.copytree(src_path,dst_path)):
            print("Directory copied succesfully")
            return True
    else:
        print("Source path/file does not exist")
        return False

def dest_path_join(dst_path,dst_ip):
    full_path="\\\\" + dst_ip + "\\" + dst_path
    return full_path


def copy_file(src_path,file_dst,path):
    dst_path = ""
    with open(file_dst) as fp:
        for system in fp:
            system = system.strip()
            dst_path = dest_path_join(path,system)
            _copy_file(src_path,dst_path)

def copy_dir(src_path,file_dst,path):
    dst_path =""
    with open(file_dst) as fp:
        for system in fp:
            system = system.strip()
            dst_path = dest_path_join(path,system)
            _copy_dir(src_path,dst_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy file/directory Script')
    #parser.add_argument('--help','-h', help="Provide Source path, text file with Hostnames and destination path \
                           #   Like \"copy_file -Source C:\\foo\\foo.txt -file hostnames.txt -Destination C$\\foo\\foo.txt\"")
    parser.add_argument('--src','-s',help="Provide the file path you want to copy. Ex: c:\\foo\\foo.txt ")
    parser.add_argument('--dst','-d',help="Provice the path you want the file to be copied. Ex: C$\\foo\\foo.txt")
    parser.add_argument('--text','-t',help="File of hostnames you want to copy")
    parser.add_argument('--file','-f',action='store_true',help="Copy file")
    parser.add_argument('--dir',action='store_true',help="Copy a directory")
    args= parser.parse_args()
    if(args.file):
        copy_file(args.src,args.text,args.dst)
    elif(args.dir):
        copy_dir(args.src,args.text,args.dst)
    else:
        print("add in argument -f for file or --dir for directory")

    

        
