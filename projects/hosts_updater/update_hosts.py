# coding=utf8
import urllib2

hosts_list = [
    "https://raw.githubusercontent.com/racaljk/hosts/master/hosts",
    "http://blog.my-eclipse.cn/hosts.txt"
]
local_hosts = "C:\\Windows\\System32\\drivers\\etc\\hosts"


def start_box():
    title = "Hosts Updater"
    padding = {
        "left": 10,
        "right": 10,
        "top": 1,
        "bottom": 1
    }
    screen_width = len(title) + padding["left"] + padding["right"] + 2

    # 输出顶部边框
    print "#" + "=" * (screen_width - 2) + "#"
    # 输出title上方的空行
    for num in range(padding["top"]):
        print "|" + " " * (screen_width - 2) + "|"
    # 输出title信息
    print "|" + " " * padding["left"] + title + " " * padding["right"] + "|"
    # 输出title下方的空行
    for num in range(padding["top"]):
        print "|" + " " * (screen_width - 2) + "|"
    # 输出底部边框
    print "#" + "=" * (screen_width - 2) + "#"

def warn_tips():
    print u"""
注意：更新会覆盖现有Hosts文件，
如Hosts存在重要内容，请备份后再使用。\n"""
    print u"是否开始执行更新？(Y/N)"
    answer = raw_input("> ").lower()

    if answer == "y":
        update_hosts()
    elif answer == "n":
        print "Bye!"
        exit(0)
    else:
        warn_tips()


# 从更新源获取hosts文件信息
def fetch_hosts_content(hosts_urls):
    content = None

    for index in range(len(hosts_urls)):
        url = hosts_list[index]
        try:
            print u"[状态] 连接 %s ......" % url
            res = urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code == 404:
                # print u"[错误] %s" % e.reason
                print u"[信息] 更新源不存在 %s" % url
                if index == len(hosts_urls) - 1:
                    print u"[状态] 更新失败:("
                    exit(1)
                else:
                    print u"[信息] 正在连接下一个更新源......"
        else:
            if res.getcode() == 200:
                print u"[信息] 连接成功......"
                content = res.read()
                break;

    return content

# 写入内容
def write_hosts(content):
    if content == None:
        print u"[状态] 更新失败:("
        exit(0)
    else:
        print u"[状态] 开始更新本地Hosts文件......"
        file = open(local_hosts, "w")
        file.write(content)
        file.close()
        print u"[状态] 更新完毕:D"

# 更新hosts
def update_hosts():
    print
    content = fetch_hosts_content(hosts_list)
    write_hosts(content)
    wait = raw_input(u"> 按任意键退出".encode("gbk"))
    exit(0)

# 程序入口
def run():
    start_box()
    warn_tips()

run()
