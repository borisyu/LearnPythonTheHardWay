# coding=utf8
# Execrise 20: Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

# file.seek(offset)
# 函数用于移动文件读取指针到指定位置
# offset值>=0
#
# 由于执行完上面print_all(current_file)后，指针在整个文件的末尾
# 必须将指针重置到文件开头file.seek(0)
# 下面的print_a_line()函数才能读取内容，否则读取出来的内容为空
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)