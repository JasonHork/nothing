def transform_back(n, i):
    result = 0
    n_1, n_2 = str(n).split('.')
    n_1_len = len(n_1)
    for a in n_1:
        n_1_len -= 1
        result += int(a)*i**n_1_len
    for b in n_2:
        n_1_len -= 1
        result += int(b)*i**n_1_len
    return result


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


num_bin = float(input('please input a binary number:'))
res_1 = int(transform_back(num_bin, 2))
print(res_1)
res_oct = transform(res_1, 8)
res_hex = transform(res_1, 16)
print(f'{num_bin}的8进制数是{res_oct}')
print(f'{num_bin}的16进制数是{res_hex}')
