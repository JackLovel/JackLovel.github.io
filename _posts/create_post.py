import time
import os

def create_file(file):
    dir = os.getcwd()
    path = os.path.join(dir, file)
    if os.path.exists(path):
        print("{0}警告!{0}\n {1} 文件已经存在\n{0}警告!{0}"
              .format("="*10, file))
    else:
        os.system("touch {}".format(file))
    
def main():
    while True:
        name = input("请输入文件名（不需要输入文件的后缀名）\n输入 q 或者 Q 取消输入: ")
        if name == "q" or name == "Q":
            break
        else: 
            create_time = time.strftime("%Y-%m-%d", time.localtime())
            suffix = ".md"
            name = create_time + "-" + name + suffix
            create_file(name)

main() 
