# 接口名称：登陆成功后修改密码
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/reset_password.do
# 接口参数：1.passwordOld 2.passwordNew
# 接口返回结果：1.密码更新成功 2.旧密码错误 3.密码更新失败
import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestResetPassword(unittest.TestCase):
    def setUp(self) -> None:
        url="http://192.168.157.129:8080/jwshoplogin/user/login.do"
        userinfo = {"username":"张明",
                    "password":"111111"}
        response = requests.post(url, data=userinfo)
        self.token = dict(response.cookies)
        # print(self.token)
        # print(response.text)

    # 定义测试方法
    def test_reset_password(self):
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        filename = p1 + "\\testdatafile\ind_interface\\test_reset_password.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        passwordinfo = {}
        # print(self.token)
        i = 0
        for row in table:
            if i > 0:
                url = row[0]
                passwordinfo["passwordOld"] = row[1]
                passwordinfo["passwordNew"] = row[2]
                response = requests.post(url, data=passwordinfo, cookies=self.token).text
                # print(response)
                self.assertIn(row[3], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestResetPassword("test_reset_password"))
    filename = r"D:\python\interfaceframe\testresultfile\ind_interface_report\reset_password.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="登陆成功后修改密码测试报告")
    runner.run(suite)
    fp.close()
