# coding=utf8

# 遍历字典元素
# 普通遍历
person = {"name": "Boris", "age": 26}
for prop in person:
    print "His %s is %s" % (prop, person[prop])

print

# 使用序列解包
for key, value in person.items():
    print "His %s is %s" % (key, value)

print


# 并行迭代
countries = ["China", "USA", "UK", "Japan"]
brands = ["Apple", "Samsung", "OPPO"]
phones = ["iPhone", "Galaxy S7", "R9"]

# zip() 将多个序列压缩到一个元组序列表中
# zip(countries, brands, phones)  -->  [("China", "Apple", "iphone"), ("USA", "Samsung", "Galaxy S7"), ("UK", "OPPO", "R9")]
for country, brand, phone in zip(countries, brands, phones):
    print "%s sales %s in %s" % (brand, phone, country)

print

# 列表推导式
# 打印0-9的平方列表
print [x*x for x in range(10)]
# 打印0-9中被3整除的数字的平方列表
print [x*x for x in range(10) if x % 3 == 0]
# 打印x轴和y轴长度都为3的坐标点
print [(x,y) for x in range(3) for y in range(3)]
