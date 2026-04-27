from sys import argv # 从sys库中调用argv变量

script, filename = argv # 解包argv列表到两个变量

txt = open(filename) # 打开filename文件，返回文件对象

print(f"Here's your file {filename}:") # 打印
print(txt.read()) # 读取并打印文件内容

print("Type the filename again:") # 打印：请求用户再次输入文件名
file_again = input("> ") # 通过 input 获取用户输入

txt_again = open(file_again) # 打开文件

print(txt_again.read()) # 读取并打印文件内容