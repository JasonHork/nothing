def transform(n, i):
    dic = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']))
    num = n
    result = []
    while True:
        if num == 0:
            break
        rest = num % i
        result.append(dic[rest])
        num = num // i
    return ''.join(list(reversed(result)))


number = int(input('please input a number:'))
print(f'{number}的2进制数是{transform(number, 2)}')
print(f'{number}的8进制数是{transform(number, 8)}')
print(f'{number}的16进制数是{transform(number, 16)}')
