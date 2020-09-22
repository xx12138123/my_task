import json
from urllib import request
import time

def encrypt(text,offset):
    result = []
    for i in list(text):
        result.append(chr(ord(i) + offset))
    return "".join(result)

def task_1():
    print("以下是任务一：凯撒加密")
    str_input = input("请输入加密内容：\n")
    while True:
        if len(str_input) == 0:
            str_input = input("哥们，输入点东西呗~")
        else:
            break

    print("请输入偏移量，默认为3（不输入使用默认，支持输入正负整数，输入0就没什么意思了）")
    offset = 3
    while True:
        try:
            str_offset = input()
            if len(str_offset) != 0:
                offset = int(str_offset)
            break
        except Exception as e:
            print("输入整数，亲~", e)
    print("经过加密，输出为：", encrypt(str_input, offset))

def task_1_add():
    print("解密什么的，在原基础上修改偏移量正负数就好了 ^_^!")

download_progress = 0
def download_callback(blocknum, blocksize, totalsize):
    global download_progress
    download_now = (blocknum * blocksize * 10) / totalsize
    download_now = int(download_now)
    if download_now > download_progress:
        download_progress = download_now
        print("=",end="")
    if download_now == 10:
        print(">")

def task_2():
    #————关于Bing的每日一图，网上已经提供了接口，就不用抓包了————
    print("任务二：下载Bing的每日一图~~") #使用自带的urllib就不用安装依赖了，虽然使用起来麻烦
    save_name = input("请输入图片名字，不使用则使用默认名字\n")
    if len(save_name) == 0:
        str_time = time.strftime("%Y-%m-%d", time.localtime())
        save_name = "Bing每日一图 " + str_time + ".jpg"
    elif not save_name.endswith("jpg"):
        save_name = save_name + ".jpg"

    print("下载中……")


    json_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    photo_url = "https://cn.bing.com/th?id=OHR.Matamata_ZH-CN8111830275_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"

    while True:
        try:
            request.urlretrieve(photo_url, "./" + save_name, download_callback)

            data = request.urlopen(json_url).read()
            json_data = data.decode('utf-8')
            json_data = json.loads(json_data)
            break
        except Exception as e:
            print("下载失败！")
            input("按任意键重试")

    print(json_data["images"][0]["copyright"])

print("这是后台第一轮考核的程序")
task_1()
task_1_add()
print()
task_2()
print("任务结束~~~")