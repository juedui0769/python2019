# 调用外部命令
# https://docs.python.org/3/library/subprocess.html

import subprocess, os

def test02():
    # https://baijiahao.baidu.com/s?id=1617741196740621222&wfr=spider&for=pc
    # os.system()
    # os.popen()
    pass

def test01():
    # https://www.jianshu.com/p/430c411160f8
    # _result = subprocess.run("echo hell0world") # 报错
    _result = subprocess.run("echo hell0world", shell=True, check=True)
    print(_result)
    # _result = subprocess.run("dir", shell=True, check=True)
    # print(_result)

def main():
    test01()
    # test02()

if __name__ == '__main__':
    main()