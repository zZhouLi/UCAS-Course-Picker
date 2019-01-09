import requests
import time
from bs4 import BeautifulSoup
import sys


class Config:
    username = "your_email@email.com"
    password = "your_passeord"
    courses = { 
        # "course_code":"dept_id"  
        # like:     "156560": "964"
    }
    
    
class Course:
    sep_host = "http://sep.ucas.ac.cn/"
    url_login = sep_host + "slogin"
    app_pick = sep_host + "/portal/site/226/821"
    course_host = "http://jwxk.ucas.ac.cn"
    course_pick_page = course_host + "/courseManage/main"
    course_save = '/courseManage/saveCourse?s='


def get_cur_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def pick_course(session):
    page_pick = session.get(Course.course_pick_page)
    soup = BeautifulSoup(page_pick.text, features="html.parser")
    pick_url = soup.find("form", id="regfrm2")["action"]

    identity = pick_url.split("?s=")[1]
    print(identity)
    count = 0
    for c_id, dept_id in Config.courses.items():
        if c_id in page_pick.text:
            count += 1
            print(get_cur_time(), "【课程号】:" + c_id + " 已选！")
            continue
        else:
            print(get_cur_time(), "开始抢课" + "【课程号】:" + c_id)
            save_url = Course.course_host + Course.course_save + identity
            data = {
                'deptIds': dept_id,
                'sids': c_id
            }
            r_save = session.post(save_url, data)
            print(save_url)
            soup = BeautifulSoup(r_save.text, features="html.parser")
            print(soup.find("body").text.strip())
    if count == len(Config.courses.items()):
        print(get_cur_time(), "所有课程都已经选上")
        sys.exit(0)


def open_pick_page(session):
    print(get_cur_time(), "正在打开选课主页")
    app_pick = session.get(Course.app_pick)
    if "Identity" in app_pick.text:
        url_redict = app_pick.text.split("window.location.href='")[1].split("'")[0]
        print(get_cur_time(), "正在跳转至:" + url_redict)
        session.get(url_redict)
    else:
        print(get_cur_time(), "跳转选课网站时失败")

    while True:
        pick_course(session)


def login():
    session = requests.Session()
    data = {
        'userName': Config.username,
        'pwd': Config.password,
        'sb': 'sb'
    }
    print(get_cur_time(), "正在登录主页")
    r_sep_slogin = session.post(Course.url_login, data=data)
    soup = BeautifulSoup(r_sep_slogin.text, features="html.parser")
    title = soup.find("li", title="当前用户所在单位")
    if title:
        name = title.text
        name = name.strip()[-3:]
        print(get_cur_time(), "用户【" + name + "】登录成功")
    else:
        print(get_cur_time(), "登录失败")
        sys.exit(-1)
    open_pick_page(session)


def main():
    login()


if __name__ == "__main__":
    main()
