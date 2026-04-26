# 导入random模块，用于随机打乱
import random

# 打开 ex7.py 文件读取
with open('ex7.py') as f:
    # 读取所有行，但过滤掉空行和注释行
    # l.strip()去掉首尾空白，如果结果非空则保留
    # not l.strip().startswith('#') 排除# 开头的注释行
    lines = [l for l in f if l.strip() and not l.strip().startswith('#')]

# 随机打乱行的顺序
random.shuffle(lines)

# 打开（或创建）ex7_broken.py 文件，写入打乱后的代码
with open('ex7_broken.py', 'w') as f:
    f.writelines(lines)

# 打印提示信息
print("Done! Try to fix ex7_broken.py")