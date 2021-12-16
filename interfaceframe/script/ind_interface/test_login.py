# 接口测试名称：用户登录接口
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/login.do
# 接口参数：1.username 2.password
# 接口返回结果：1.登录成功 2.用户名不存在 3.密码错误
import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestLogin(unittest.TestCase):
    def test_login(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/login.do"
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        # print(p1)
        filename = p1 + "\\testdatafile\ind_interface\\test_login.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i > 0:
                userinfo["username"] = row[0]
                userinfo["password"] = row[1]
                # print(userinfo)
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[2], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    filename = "D:\python\interfaceframe\\testresultfile\ind_interface_report\\login_report.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="用户登录测试报告")
    runner.run(suite)
    fp.close()
