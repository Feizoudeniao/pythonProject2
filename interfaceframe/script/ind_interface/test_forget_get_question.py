# 接口名称：忘记密码提示密保接口
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/forget_get_question.do
# 接口参数：1.username
# 接口返回结果：1.密保问题 2.用户不存在 3.找回密码问题失败
import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestForgetGetQuestion(unittest.TestCase):
    def test_forget_get_question(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/forget_get_question.do"
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        filename = p1 + "\\testdatafile\ind_interface\\test_forget_get_question.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i > 0:
                userinfo["username"] = row[0]
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[1], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestForgetGetQuestion("test_forget_get_question"))
    filename = "D:\python\interfaceframe\\testresultfile\ind_interface_report\\forget_get_question.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="忘记密码提示密保接口测试报告")
    runner.run(suite)
    fp.close()
