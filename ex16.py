# 从 sys 模块导入 argv 列表，用于获取命令行参数
from sys import argv 

# 将 argv 解包到 script（脚本名）和filename（要操作的文件名）两个变量
script, filename = argv

# 打印警示信息，告知用户将要清空哪儿个文件
print(f"We're going to erase {filename}.")
# 提示用户按 Ctrl+C 取消操作
print(f"If you don't want that, hit CTRL-C (^C).")
# 提示用户按回车确认继续
print(f"If you do want that, hit RETURN.")

# 等待用户输入，按回车继续，按Ctrl+C中断程序
input("?")

# 以写入模式（'w'）打开文件，这会清空原有内容
print("Opening the file...")
target = open(filename, 'w')

# 显式调用truncate（）截断文件（实际上'w'模式已清空，此行多余但无害）
print("Truncating the file. Goodbye!")
target.truncate()

# 提示用户输入三行内容
print("Now I'm going to ask you for three lines.")

# 获取用户输入的三行文本
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# 告知用户即将写入文件
print("I'm going to write these to the file.")

# 逐行写入文件，每行后加换行符
target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# 告知用户即将关闭文件
print("And finally, we close it.")

# 关闭文件，释放资源，确保数据写入磁盘
target.close()

# 告知用户即将打印文件内容
print("I'm going to print the file.")
print(f"Here's your file {filename}:")

# 读取文件
txt = open(filename)
print(txt.read())
txt.close()

