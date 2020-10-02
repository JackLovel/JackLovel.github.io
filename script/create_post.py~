import time
import os

def create_file(file):
    dir = os.getcwd()
    path = os.path.join(dir, file)
    if os.path.exists(path):
        print("{0}warning!{0}\n {1} is exists\n{0}warning!{0}"
              .format("="*10, file))
    else:
        os.system("touch {}".format(file))
    
def main():
    name = input("please enter file name:")
    create_time = time.strftime("%Y-%m-%d", time.localtime())
    suffix = ".md"
    name = create_time + "-" + name + suffix
    create_file(name)

    
main() 
