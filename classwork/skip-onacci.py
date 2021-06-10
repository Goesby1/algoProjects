def skiponacci(n) -> int:
    
    if (n == 1 ):
        return 0
    elif (n == 2 or n == 3):
        return 1
    return skiponacci(n - 1) + skiponacci(n - 3)


if __name__ == "__main__":
    print(skiponacci(4), skiponacci(10))
