# coding=utf8
# Exercise 13 Parameters, Unpacking, Variables

# 写一个可以接受参数的脚本
from sys import argv

# script, first, second, third = argv
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
Your live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)