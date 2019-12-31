#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


# mode=1时获取当前所有包，否则只获取有更新的包
def get_list(mode=None):
    print('正在获取pak列表……')
    command = 'pip list' if mode == 1 else 'pip list -o'
    pak_list = [pak.split()[0] for pak in os.popen(command).readlines()[2:]]
    print('获取pak列表成功！一共有 %d 个包' % len(pak_list))
    return pak_list


# mode=1时为安装模式，否则为升级模式
def update_pak(pak_list, mode=None):
    command = 'pip install ' if mode == 1 else 'pip install --upgrade '
    print('开始更新/安装 %d 个包……' % len(pak_list))
    for pak in pak_list:
        os.system(command + pak)


def main():
    ask = input('1.更新所有已安装的包；2.导入安装包；3.导出安装包\n请选择您要执行的操作：')
    if ask == '1':
        pak_list = get_list()
        if len(pak_list) != 0:
            update_pak(pak_list)
        else:
            print('已经没有可更新的包啦！请重新选择您要执行的操作')
    elif ask == '2':
        input('请确认当前运行目录下存在名为 pak_list.txt 的文件（按Enter继续）')
        try:
            with open('pak_list.txt', 'r', encoding='utf-8') as f:
                pak_list = f.read().splitlines()  # 这里用readlines会有换行符
            local_list = get_list(1)
            install_list = list(set(pak_list).difference(set(local_list)))
            if len(install_list) != 0:
                update_pak(install_list, 1)
                print('安装完成！')
            else:
                print('您已安装了所有包！')
        except Exception as e:
            print(e)
    elif ask == '3':
        input('将会在当前目录生成一个名为 pak_list.txt 的文件（按Enter继续）')
        local_list = get_list(1)
        txt = ''
        for i in local_list:
            txt += i + '\n'
        try:
            with open('pak_list.txt', 'w', encoding='utf-8') as f:
                f.write(txt)
            print('导出成功！共有 %d 个包' % len(local_list))
        except Exception as e:
            print(e)
    else:
        print('输入无效，请重新输入：')
    main()


if __name__ == '__main__':
    main()

