# update-pip-list
可以批量更新pip list



平时会在好几台电脑上面切换，安装包就不同步；或者一段时间之后发现要升级好多个包，逐个pip install太麻烦了

搞了个简单的小工具

windows下执行update.bat即可

linux下可以直接cd到这个目录下，输入python3 update-pip-list.py执行；也可以输入sh update.sh执行



选项1是更新现有需要更新的包

选项2是导入，需要在当前目录下有一个叫pak_list.txt的文件（开始之后会先获取当前电脑里的pip list，在安装的时候自动跳过已经装过的）

选项3是导出，获取当前电脑的pip list，放在生成的pak_list.txt里面



需要同步两台电脑的环境时可以在a电脑先按3导出，然后把pak_list.txt文件拷到b电脑上去再运行2导入即可

