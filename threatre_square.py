def threatre_square(n, m, a):
    if n % a != 0:
        n = n+(a-(n % a))
    if m % a != 0:
        m = m+(a-(m % a))
    return (n*m)//(a**2)


if __name__ == '__main__':
    size = input().split(" ")
    n = int(size[0])
    m = int(size[1])
    a = int(size[2])
    result = threatre_square(n, m, a)
    print(result)
