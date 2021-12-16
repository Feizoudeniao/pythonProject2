# 接口测试名称：用户注册接口
# 请求方法：post
# 请求地址：http://192.168.157.129:8080/jwshoplogin/user/register.do
# 接口测试参数：1.username 2.password 3.email 4.phone 5.question 6.answer
# 接口预期结果：1.注册成功 2.用户名已经存在 3.邮件已经存在 4.注册失败

import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestRegister(unittest.TestCase):
    def test_register(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/register.do"
        path = os.getcwd()
        # print(path)
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        # print(p1)
        filename = p1 + "\\testdatafile\ind_interface\\test_register.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i > 0:
                userinfo["username"] = row[0]
                userinfo["password"] = row[1]
                userinfo["email"] = row[2]
                userinfo["phone"] = row[3]
                userinfo["question"] = row[4]
                userinfo["answer"] = row[5]
                # print(userinfo)
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[6], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    # unittest.main()

    # 声明测试套
    suite = unittest.TestSuite()
    # 通过addTest方法添加测试用例
    suite.addTest(TestRegister("test_register"))
    # 定义测试报告文件
    file = "D:\python\interfaceframe\\testresultfile\ind_interface_report\\register_report.html"
    # 以wb的方式打开文件
    fp = open(file, "wb")
    # 调用HTMLTestRunner测试报告的报告生成测试报告
    runner = HTMLTestRunner(stream=fp, title="用户注册测试报告")
    # 执行测试套
    runner.run(suite)
    fp.close()
