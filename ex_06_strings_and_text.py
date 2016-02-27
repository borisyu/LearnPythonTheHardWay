#coding=utf8
# 习题6：字符串和文本 Strings and Text

# format string 格式化字符串
# % 是格式化操作符
# %s 字符串（采用str()的显示）
# %r 字符串（采用repr()的显示）
# %c 单个字符及ASCII码
# %(name) 引用字典中的元素，name为字段元素名
# %b 二进制整数 b for binary
# %o 八进制整数 o for octonary
# %d 十进制整数 d for decimal
# %i 十进制整数
# %x 十六进制整数 x for hexadecimal
# %e 指数（基底写为e）
# %E 指数（基底写为E）
# %f 浮点数
# %F 浮点数
# %g 指数(e)或浮点数
# %G 同上
# %% 字符"%"

types_of_people = "There are %d types of people." % 10
binary = "binary"
do_not = "dont't"
knows_about_binary = "Those who know %s and those who %s" % (binary, do_not)

print types_of_people
print knows_about_binary
print "\r"
print "I said: %r." % types_of_people
print "I also said: '%s'." % knows_about_binary
print "\r"

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
print "\r"

w = "This is the left siade of..."
e = "a string with a right side."
print w + e