def plusMinus(arr):
    neg = zero = poz = 0
    for num in arr:
        if num < 0:
            neg += 1
        elif num > 0:
            poz += 1
        else:
            zero += 1
    print(poz/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
