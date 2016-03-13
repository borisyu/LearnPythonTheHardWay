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

convertDatetime()


# Code list 2-3 序列（字符串）乘法示例
def printBox():
    sentence = raw_input("Sentence: ")

    screen_width = 60
    text_width = len(sentence)
    box_width = text_width + 4
    left_margin = (screen_width - box_width) // 2

    print 'Screen Width:', screen_width
    print 'Text Width:', text_width
    print 'Box Width:', box_width
    print 'Margin Left:', left_margin

    print
    print ' ' * left_margin + '#' + '=' * (box_width - 2) + '#'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '| ' + sentence + ' |'
    print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
    print ' ' * left_margin + '#' + '=' * (box_width - 2) + '#'
    print

printBox()