from sys import argv # 从sys模块中导入argv列表

script, input_file = argv # 解包argv：脚本名和输入文件名

# 定义函数，打印文件全部内容
def print_all(f):
    print(f.read())

# 定义函数，将文件光标移回开头
def rewind(f):
    f.seek(0)

# 定义函数，功能为打印一行文件内容
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 打开文件，返回文件对象
current_file = open(input_file)

# 打印提示：首先打印全部文件内容
print("First let's print the whole file:\n")

# 调用函数，打印文件全部内容
print_all(current_file)

# 打印提示：现在像磁带一样倒带回到首行
print("Now let's rewind, kind of like a tape.")

# 调用函数，回到文件首行
rewind(current_file)

# 打印提示
print("Let's print three lines:")

# 定义现在的行数，并调用函数，依此打印
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)