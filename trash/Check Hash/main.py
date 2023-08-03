# https://www.cyberforum.ru/python-tasks/thread3005616.html?ysclid=lcgcglduyg120846680
# программу, которая будет проверять четвертый файл с хэшами из 3 файлов, на наличие изменений хэшэй тех трех файлов

import hashlib

file_hash_name = "hash.txt"
files_names = ["file1.txt", "file2.txt", "file3.txt"]

files_info = {}

try:
    with open(file_hash_name, "rt", encoding="utf-8") as file:
        for line in map(str.strip, file):
            file_name, file_hash = map(str.strip, line.split(";"))
            files_info[file_name] = file_hash
except FileNotFoundError:
    ...

for file_name in files_names:
    with open(file_name, "rb") as file:
        file_hash = hashlib.sha256(file.read())
        file_hash_hex = file_hash.hexdigest()
        if file_hash_hex != files_info.get(file_name, file_hash_hex):
            print(f"Не совпал хеш у файла: {file_name}")
        files_info[file_name] = file_hash_hex

with open(file_hash_name, "wt", encoding="utf-8") as file:
    for file_name, file_hash in files_info.items():
        file.write(f"{file_name};{file_hash}\n")