def domino(a,b):
    return (a*b)//2

if __name__ == '__main__':
    size = input().split(" ")
    m=int(size[0])
    n=int(size[1])
    result = domino(m,n)
    print(result)
