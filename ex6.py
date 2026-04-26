# types_of_people = 10 # 定义变量，值为整数10

# # 定义字符串x，用f-string 嵌入 type_of_people 的值
# x = f"There are {types_of_people} tpyes of people." 

# binary = "binary" # 定义字符串binary，值为“binary”
# do_not = "don't" # 定义字符串do_not，值为“don‘t”
# # 定义字符串y，用f-string 嵌入binary 和 do_not
# y = f"Those who know {binary} and those who {do_not}"

# print(x) # 打印x
# print(y) # 打印y

# print(f"I said: {x}") # 打印字符串，又在里面嵌入了x
# print(f"I also said: '{y}'") # 打印字符串，又在里面嵌入了y

# hilarious = False # 定义布尔变量hilarious，值为False

# # 定义字符串joke_evaluation，里面有一个{}占位符
# joke_evaluation = "Isn't that joke so funny?! {}" 

# # 用.format()方法把hilarious填入占位符
# print(joke_evaluation.format(hilarious))


# w = "This is the left side of ..." # 定义字符串w
# e = "a string with a right side." # 定义字符串e

# print(w + e) # 用 + 连接两个字符串，打印结果

# 打乱练习
types_of_people = 10
do_not = "don't"
binary = "binary"
hilarious = False  # 注意：字符串而非布尔值！
joke_evaluation = "Isn't that joke so funny?! {}"

x = f"There are {types_of_people} types of people."
y = f"Those who know {binary} and those who {do_not}."
w = "This is the left side of..."
e = "a string with a right side."

print(x)
print(w + e)
print(f"I said: {x}")
print(f"I also said: '{y}'")
print(joke_evaluation.format(hilarious))

