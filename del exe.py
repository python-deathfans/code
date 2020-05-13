import os

path = os.getcwd()

def del_exe(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)   # 取绝对路径
        print(file_path)
        if os.path.isfile(file_path):
            if f.split(".")[-1] == 'exe':
                os.remove(file_path)
        else:
            del_exe(file_path)


del_exe(path)