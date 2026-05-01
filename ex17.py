from sys import argv # 从 sys 模块导入 argv 列表，用于获取命令行参数
from os.path import exists # 从 os.path 模块导入 exists

# 将 argv 解包到 script（脚本名）, from_file, to_file三个变量
script, from_file, to_file =argv 

# print(f"Copying from {from_file} to {to_file}") # 打印

# we could do these two on one line, how?
# in_file = open(from_file) # 打开from_file
# indata = in_file.read() # 
# indata = open(from_file).read() # 读取源文件

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}") # 检查目标文件是否存在
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")

open(to_file, 'w').write(open(from_file).read())
print(open(to_file).read())
# in_file.close()


