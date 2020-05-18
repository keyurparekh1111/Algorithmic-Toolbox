# Uses python3
def gcd(a, b):
    while b != 0:
        c = a%b
        a,b = b,c
    return a

def lcm(a, b):
    div = gcd(a,b)
    print(int(a*b/div))


if __name__ == '__main__':
    a, b = map(int, input().split())
    lcm(a, b)
