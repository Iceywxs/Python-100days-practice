def main():
    row=int(input('请输入行数：'))

    for i in range(row):
        for j in range(i+1):
            print('*',end='')
        print()

    #print默认是打印一行，结尾加换行。end = ' '意思是末尾不换行，加空格
    for i in range(row):
        for j in range(row):
            if j<row-i-1:
                print(' ',end='')
            else:
                print('*',end='')
        print()

    for i in range(row):
        for j in range(row-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print('*',end='')
        print()




if __name__ == '__main__':
    main()