#coding=utf8

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

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Bue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %r." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %i." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print "\r"

my_words = "now is better than never"