# 李双博
# 学习python
# 开发时间 2021/12/23  16:51
import requests
from base64 import b64encode
from Cryptodome.Cipher import AES
import json
#
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
d_pre_data = {
    #加密前的参数
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "A_PL_0_6964646956",
    "threadId": "A_PL_0_6964646956"

}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'WSjpSRm1ujF8bgo9'
def get_encSecKey():  #i = "WSjpSRm1ujF8bgo9"时  encSecKey是定值，由此可得请求中第二个参数
    return "49646fa4d36d9ab1d29b76d1e732540bb720d40971527b4566096d67bc580505f7ac4cb155b38cc934119b59ed5bfd059b6239843484528f8a274d6a4971f0a06fb89661534ffb8a3c8c1bf28ce486781dc63b8d9bc61bcc8636014a8a0ad0bd85f559acba00e686b733f2a1a52e491ed7421e20dc7fd7aee0f149df1689b3b0"

def str_to16(data):  #加密算法中所有参数长度必须是16位的倍数，不满16位的差X位就补齐X位，用chr(X)来补齐，等于16位的需要补16位
     pad =  16 - len(data) % 16
     data += chr(pad) * pad
     return data

def encrypt_data(data,key): #AES加密算法
    iv = "0102030405060708".encode('utf-8')   #偏移量
    aes = AES.new(key=key.encode('utf-8'),mode=AES.MODE_CBC,iv=iv)   #创建加密器
    data = str_to16(data)                           #将请求数据补齐至16的倍数
    enc_data = aes.encrypt(data.encode('utf-8'))    #加密
    enc_data_str = str(b64encode(enc_data),'utf-8') #加密后的数据是字节，将字节转化为字符串，此处无法使用utf-8只能用base64编码

    return enc_data_str

def get_data():
    first = encrypt_data(json.dumps(d_pre_data),g)
    second = encrypt_data(first,i)
    return second

data_param = {
    # 加密后的参数
    'params': get_data(),
    'encSecKey': get_encSecKey()
}

resp = requests.post(url,data=data_param)
print(resp.json())

# function
# a(a)    a函数的作用就是得到一个16位的由数字和字母组成的随机字符串
# {
#     var
# d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
# for (d = 0; a > d; d += 1)
# e = Math.random() * b.length,     获取随机数
#     e = Math.floor(e),            将上面随机数取整
#         c += b.charAt(e);         得到一个16位的由数字和字母组成的随机字符串
# return c
# }
# function
# b(a, b)
# {
# var
# c = CryptoJS.enc.Utf8.parse(b)     密钥
# , d = CryptoJS.enc.Utf8.parse("0102030405060708")   iv偏移量
# , e = CryptoJS.enc.Utf8.parse(a)    数据
# , f = CryptoJS.AES.encrypt(e, c, {
#     iv: d,
#     mode: CryptoJS.mode.CBC
# });
# return f.toString()
# }
# function
# c(a, b, c)
# {
# var
# d, e;
# return setMaxDigits(131),
# d = new
# RSAKeyPair(b, "", c),
# e = encryptedString(d, a)
# }
# function
# d(d, e, f, g)   d是请求数据  efg都是定值
# {
# var
# h = {}
# , i = a(16);  i就是一个16位随机生成的字符串，这里我们可以写死i，后续所有用到i的地方，都可以用这个定值。  i=WSjpSRm1ujF8bgo9
# return h.encText = b(d, g),     b方法就是加密算法   d是数据，g是定值
# h.encText = b(h.encText, i),
# h.encSecKey = c(i, e, f), i  e  f都是定制，且方法c中没有随机数，所以encSecKey必为定制，且与i对应
# h
# }












