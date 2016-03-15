# coding=utf8

# Code list 2-1 索引使用实例
def convertDatetime():
    # 根据给定的年月日以数字形式打印出日期
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    # 以1~31的数字作为结尾的列表
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

    year = raw_input('Year: ')
    month = raw_input('Month (1-12): ')
    day = raw_input('Day (1-31): ')

    month_number = int(month)
    day_number = int(day)

    # 将月份和天数-1，以获得正确的索引
    month_name = months[month_number - 1]
    ordinal = day + endings[day_number - 1]

    print month_name + ' ' + ordinal + ', ' + year

# convertDatetime()


# Code list 2-3 序列（字符串）乘法示例
def startSystem():
    sys = raw_input("Type your system: ")

    screen_width = 30
    text_width = len(sys)
    box_width = text_width + 4
    left_margin = (screen_width - box_width) // 2

    print
    print ' ' * left_margin + '#' + '=' * (box_width - 2) + '#'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '| ' + sys + ' |'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '#' + '=' * (box_width - 2) + '#'
    print

# startSystem()


# Code list 2-4 成员资格检查
def userLogin():
    database = [
        ['albert', '1234'],
        ['smith', '7524'],
        ['jones', '9843'],
        ['boris', '1024'],
        ['shawn', '9527']
    ]
    username = raw_input('User name: ')
    pin = raw_input('PIN code: ')

    if [username, pin] in database:
        print 'Access granted!'
    else:
        print 'Access denied!'

# userLogin()


def down_sort(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

nums = [5, 2, 9, 7, 7]
nums.sort(down_sort)
print nums
