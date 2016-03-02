# coding=utf8
# Exercise 40: Dictionary
#
# cities.items() 返回键值对列表  -> [(key, value), (key, value)]
# cities.get('key')  获取相应键的值
# cities.get('key', 'default value')  获取相应键的值，如果不存在该键值，则返回默认值

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print "-" * 30
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# print some states
print "-" * 30
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

# do it by using the state then cities dict
print "-" * 30
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

# print every state abbreviation
print "-" * 30
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print "-" * 30
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print "-" * 30
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "-" * 30
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city
