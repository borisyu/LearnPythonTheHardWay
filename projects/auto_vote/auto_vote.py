# coding=utf8
from PIL import Image
import StringIO
import requests
import pytesseract

vote_url = "http://www.bblxlm.com/Vote_do.asp"
img_url = "http://www.bblxlm.com/Inc/ChkCode/validatecode.asp"
img_name = "captcha.bmp"
request_header = {
    "Host": "www.bblxlm.com",
    "Origin": "http://www.bblxlm.com",
    "Referer": "http://www.bblxlm.com/vote.asp",
    "Cookie": "ASPSESSIONIDQSQSBCTR=LMCJBJEBIKJIIDDGLOEGMPLF; QQ=18929154432; MAIL=yuhaobo%40jobcn%2Ecom; name=%C5%DC%B5%F7%B5%C4%B0%FC%D7%D3"
}
payload = {
    "pid": "32,61,98,99,96",
    "name": "boris",
    "MAIL": "yuhaobo@jobcn.com",
    "QQ": "18929154432",
    "ValidCode": "",
    "xs": u"莫祉言,谢青原,翟淑欣,何宇希,宁陈林"
}

def get_verify_code_image(url):
    '''获取验证码图片'''
    print u">_获取验证码图片"
    response = requests.get(url, headers=request_header)
    i = Image.open(StringIO.StringIO(response.content))
    return i

def parse_code_to_string(image):
    print u">_解析验证码"
    valid_code = pytesseract.image_to_string(image, config="-psm 7")
    return valid_code

def vote():
    print u">_进行投票"
    response = requests.post(vote_url, data=payload, headers=request_header)
    print u">_投票结果"
    print response.text

def auto_vote():
    # 首先获取验证码
    img = get_verify_code_image(img_url)
    img.save(img_name)

    # 从验证码图片中解析出验证码信息
    valid_code = parse_code_to_string(img)

    print u">_验证码：" + valid_code

    # 设置payload验证码数据
    payload["ValidCode"] = valid_code

    # 进行投票
    vote()

auto_vote()