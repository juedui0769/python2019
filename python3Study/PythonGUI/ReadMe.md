### Tkinter

Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。

由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。

> 摘自: <https://www.runoob.com/python/python-gui-tkinter.html> 菜鸟教程

> <https://blog.csdn.net/ahilll/article/details/81531587> 这篇更详细

### 安装（windows）

from : <https://wiki.python.org/moin/TkInter>

```
workon py3
python
import _tkinter
```

If it fails with "No module named _tkinter", your Python configuration needs to be modified to include this module (which is an extension module implemented in C). Do **not** edit Modules/Setup (it is out of date). You may have to install Tcl and Tk (when using RPM, install the -devel RPMs as well) and/or edit the setup.py script to point to the right locations where Tcl/Tk is installed. If you install Tcl/Tk in the default locations, simply rerunning "make" should build the _tkinter extension.

## PyQt5

```
workon py3
pip config list
pip search pyqt5
```

> PyQt5 (5.14.0)                    - Python bindings for the Qt cross platform application toolkit

```
pip install PyQt5
```



