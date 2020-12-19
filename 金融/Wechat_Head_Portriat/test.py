import os

pwd = os.getcwd()
print(pwd)

os.chdir("./avatar")
pwd = os.getcwd()

print(pwd)