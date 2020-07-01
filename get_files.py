import os

def show_files(path,cur_file_list):
    """
    获取递归列表文件夹下，所有文件    
    """
    
    
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, cur_file_list)
        else:
            print(cur_path)
            cur_file_list.append(cur_path)
    return cur_file_list

# 传入空的list接收文件名
cur_files= show_files("/data/algorithm/dongyang/seqH8/dy_test/01tif/2019/",[])
# 循环打印show_files函数返回的文件名列表
for cur_file in cur_files:
    print(cur_file)
