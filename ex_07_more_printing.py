# coding=utf8
# 习题7：打印更多 More Printing

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print 'And everywhere that Mary went.'
print "." * 6 # 重复打印6次

print "\r"

print "Mary had a little lamb.",
print "Its fleece was white as %s." % 'snow',
print 'And everywhere that Mary went.',
print "." * 6 # 重复打印6次

# 以上两种输出形式
# ","起到输出一个空白字符的作用
# print ,  <--- 这样的语句是会报错的，因为逗号并非变量，无法输出
# print "",  <--- 这样可以运行

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print "\r"
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12