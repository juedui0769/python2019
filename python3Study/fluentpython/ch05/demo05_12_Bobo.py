import bobo

# 我在windows下运行本示例，步骤如下：
# win + R : cmd 进入到控制台
# workon py3 进入到 py3 对应的虚拟机
# bobo --help 看看 bobo 是否安装
# bobo -f demo05_12_Bobo.py  默认启动在8080
# 右键打开 Git 自带的 Bash 使用 curl 访问localhost 8080
# curl -i http://localhost:8080/
# curl -i http://localhost:8080/?person=Jim
# 运行上面的两条指令查看输出

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person