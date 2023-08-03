# https://russianblogs.com/article/88462147886/
# определение дубликатов файлов

import os
import hashlib

path_s = 'C:\\Users\\User\Downloads\Telegram Desktop\Email Private   [httpst.meemailprivate]'  # с чем сравнивать

path_t = 'D:\[.Telega_dBase]\Email Private   [httpst.meemailprivate]'  # откуда сравнивать
path_t2 = 'D:\\.Unic'  # куда копировать
list_file = {}


def create_file_list(path):
    for name in os.listdir(path):
        filename = path + os.sep + name
        if os.path.isdir(filename):
            create_file_list(filename)
        else:
            with open(filename, 'rb') as f:
                #md5 = hashlib.md5(f.read()).hexdigest()
                md5 = hashlib.sha256(f.read()).hexdigest()
                print(filename, md5)
                if md5 not in list_file:
                    list_file[md5] = 1


def copy_file(paths, patht):
    for filename in os.listdir(paths):
        filename_s = paths + os.sep + filename
        filename_t = patht + os.sep + filename
        #if os.path.isdir(filename_s):
        #    if not os.path.exists(filename_t):
        #        os.mkdir(filename_t)
        #    copy_file(filename_s, filename_t)
        #else:
            #if os.path.exists(filename_t):
            #    print('[*] "%s" already exists! ' % filename_t)
            #else:
        with open(filename_s, 'rb') as f_s:
            data = f_s.read()
            #file_md5 = hashlib.md5(data).hexdigest()
            file_md5 = hashlib.sha256(data).hexdigest()
            if file_md5 not in list_file:
                list_file[file_md5] = 1
                print('[*]  Source :', filename_s)
                print('[*]  Target :', filename_t)
                with open(filename_t, 'wb') as f_t:
                    f_t.write(data)
            else:
                print('[*] "%s"\'s MD5 already exists! ' % filename_t)


create_file_list(path_t)
copy_file(path_s, path_t2)
