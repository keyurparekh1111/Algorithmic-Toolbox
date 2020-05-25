# Uses python3

def get_change(m):
    #write your code here
    count=0;
    while m!=0:
        if(m>=10):
            m=m-10;
        elif(m>=5):
            m=m-5;
        else:
            m=m-1;
        count=count+1

    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
