# coding=utf8
# 文档化函数，在函数内部的开头写下字符串
def fibs(num):
    u'计算斐波那契数'
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print u'fibs()函数说明:', fibs.__doc__
print fibs(10)
