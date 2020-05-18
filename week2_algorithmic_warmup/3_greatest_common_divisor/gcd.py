# Uses python3
def gcd(a, b):
    while b != 0:
        c= a%b
        a,b = b,c
    print(a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd(a, b)
