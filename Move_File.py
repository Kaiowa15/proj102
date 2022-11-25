import os
import shutil

from_dir = "C:/Users/Kaiowa/Downloads"
to_dir = "C:/Byjus/imagensbaixadas"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension =="":
        continue
    if extension in ['.txt,.doc,.docx,.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_texto"
        path3 = to_dir + '/' + "Arquivos_texto" + '/' + file_name
        print("path1 " , path1)
        print("path3 ", path3)

    if os.path.exists(path2):
            print("movendo o arquivo", file_name + "[................]")

            shutil.move(path1, path3)
    else:
            os.makedirs(path2)
            print("movendo o arquivo", file_name + "[................]")
            shutil.move(path1,path3)

#tem alguma coisa dando errado mas não tenho ideia do que seja, e não tem como pegar o cominho documentos