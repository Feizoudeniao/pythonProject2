# 接口名称：检测用户名或者邮件是否有效
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/check_vaild.do
# 接口参数：1.str 2.type
# 接口返回结果：1.校验成功 2.用户名已经存在 3.邮件已经存在 4.注册参数错误
import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestCheckVaild(unittest.TestCase):
    def test_check_vaild(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/check_vaild.do"
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        filename = p1 + "\\testdatafile\ind_interface\\test_check_vaild.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i > 0:
                userinfo["str"] = row[0]
                userinfo["type"] = row[1]
                # print(userinfo)
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[2], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCheckVaild("test_check_vaild"))
    filename = "D:\python\interfaceframe\\testresultfile\ind_interface_report\check_vaild.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="检测用户名或者邮件是否有效测试报告")
    runner.run(suite)
    fp.close()
