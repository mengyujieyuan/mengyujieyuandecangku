Datas = {}
def main():
    print('1：录入 2：查询 3：删除 4：查看')
    t=input('选择：')
    if t=='1':
       n=input('请输入该生学号:')
       s=input("请输入该生成绩:")
       Datas[n] = s
    elif t=='2':
       print ('1:查询  2:退出')
       x=input('请选择:')
       if x=='1':
           y=input("请输入该生学号:")
           print(Datas[y])
       else:
           pass
    elif t=='3':
        i=input('请选择:')
        Datas.pop(i)
    else:
        for m in Datas:
            print(m,Datas[m])
while True:
    main()

