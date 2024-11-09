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


num = float(input('please input a number:'))
dec = int(input('what is the decimal system of your number?'))
print(f'{dec}进制数{num}的10进制数是{transform_back(num, dec)}')
