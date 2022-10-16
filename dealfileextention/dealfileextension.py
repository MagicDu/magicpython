import os
# 遍历文件夹
def walkFile(file):
    #print(file)
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        #print(files)
        for f in files:
            #print(f)
            #批量删除以.ev4结尾的文件           
            if f[-6:] == '.Elbie':
                 #print(f)
                #批量重命名
                old = root + '\\'+f 
                new  = root + '\\'+f.replace(".exe","")
                #print(old)
                #print(new)
                try:
                    os.rename(old,new)
                except:
                    print("error")
def main():
    walkFile("E:")
 
if __name__ == '__main__':
    main()