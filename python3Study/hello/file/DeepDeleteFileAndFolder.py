# 参考: https://blog.csdn.net/weixin_42854038/article/details/82799123
import os, shutil

def delete_dir(root_dir):
    file_list = os.listdir(root_dir)
    for f in file_list:
        filepath = os.path.join(root_dir, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(str(filepath), " removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            print("dir ", str(filepath), " removed!")
    shutil.rmtree(root_dir, True) # 只这一句就可以了

def test01():
    root_dir = "D:\\temp\\11"
    delete_dir(root_dir)

def main():
    test01()

if __name__ == '__main__':
    main()