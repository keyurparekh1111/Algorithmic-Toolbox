# Uses python3
def calc_fib(n):
    fibo=[0]*(n+1)
    fibo[1]=1

    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
    print(fibo[-1])


if __name__ == '__main__':
    n = int(input())
    if n <=1:
        print(n)
    else:
        calc_fib(n)
