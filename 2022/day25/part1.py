snafu2Digit = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

digitToSnafu = {
    -6: '--',
    -5: '-0',
    -4: '-1',
    -3: '-2',
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2',
    3: '1=',
    4: '1-',
    5: '10',
    6: '11'
}


def addSnafuDigits(d1, d2, d3):
    # return carry, result
    result = digitToSnafu[snafu2Digit[d1] + snafu2Digit[d2] + snafu2Digit[d3]]
    if len(result) == 2:
        return list(result)
    else:
        return ['0', result]


def addSnafu(s1: str, s2: str):
    N = max(len(s1), len(s2))
    s1 = s1.rjust(N, '0')
    s2 = s2.rjust(N, '0')
    result = []

    carry = '0'
    for i in range(N-1, -1, -1):
        c, r = addSnafuDigits(s1[i], s2[i], carry)
        result.append(r)
        carry = c

    result.append(carry)
    return ''.join(reversed(result)).lstrip('0')


allNums = open('input/in1.txt', 'r').read().split('\n')
result = '0'
for num in allNums:
    result = addSnafu(result, num)
print(result)
