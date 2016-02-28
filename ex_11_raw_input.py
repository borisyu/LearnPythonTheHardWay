# coding=utf8
# 习题11 Asking Questions
# raw_input() 读入用户输入的内容，返回一个字符串
# words = raw_input()
# type(words)  -->> <type 'str'>

# Windows 环境下，键入命令
# python -m pydoc raw_input
# 查看raw_input的文档说明
#
# Unix/Linux环境下，键入命令
# pydoc raw_input
# 查看raw_input的文档说明
#
# 按q退出pydoc

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "\r"

print "What kind of programing language do you use?"
language = raw_input('answers: ')
print "What kind of editor do you use?"
editor = raw_input('answers: ')

print "OK, you are a %s developer while using %s as your favorite editor." % (language, editor)