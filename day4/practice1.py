
# cmath 模块运算的是复数，math 模块运算的是数学运算
from math import sqrt

def main():
    number=int(input("请输入一个整数："))
    is_prime=True
    end=int(sqrt(number))
    for i in range(2,end+1):
        if number%i==0:
            is_prime=False
            break
    if is_prime and number!=1:
        print('%d是素数' % number)
    else:
        print('%d不是素数' % number)




if __name__ == '__main__':
    main()


