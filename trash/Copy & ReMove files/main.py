

import os, shutil

root_src_dir = r"C:\test\111\\"    #Path/Location of the source directory
root_dst_dir = "C:\\test\cop\\"  #Path to the destination folder
file_ = "qw.txt"
for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    #for file_ in files:
       # print(file_)
       # src_file = os.path.join(src_dir, file_)
       # dst_file = os.path.join(dst_dir, file_)
       #
        #if os.path.exists(dst_file):
        #    os.remove(dst_file)
        #shutil.copy(src_file, dst_dir)

    src_file = os.path.join(src_dir, file_)
    dst_file = os.path.join(dst_dir, file_)

    print(src_file)
    print(dst_file)

    if os.path.exists(dst_file):
        os.remove(dst_file)
    shutil.move(src_file, dst_dir)