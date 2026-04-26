print("Mary had a little lamb.") # 打印字符串
# 打印字符串，用.format()把'snow'填入{}位置
print("Its fleece was white as {}.".format('snow')) 
print("And everywhere thar Mary went.") # 打印字符串
print("." * 10) # what'd that do? # 打印'.'，重复十次

# 定义12个变量，每个存一个字母
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what h
# 打印前六个字母拼接，结尾不换行，加个空格
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

# 打印后六个字母拼接
print(end7 + end8 + end9 +end10 +end11 +end12)