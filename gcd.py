def gcd(a:int, b:int):
    if b == 0:
        return print(a)
    print(f'gcd({b, a%b})')
    return gcd(b, a%b)

def main():
    a:int = int(input("a: "))
    b:int = int(input("b: "))
    gcd(a, b)

if __name__ == '__main__':
    main()