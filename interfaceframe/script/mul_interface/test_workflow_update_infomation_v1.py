# 接口联调测试 共涉及四个测试方法，接口如下：
# 1.用户注册接口
# 2.用户登录接口
# 3.获取用户信息接口
# 4.更新用户信息接口

import unittest
import requests

from HTMLTestRunner import HTMLTestRunner


class WorkflowUpdateInfo(unittest.TestCase):
    # 用户注册接口
    def test_case1(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/register.do"
        registerinfo = {"username": "Lucy1",
                        "password": "123456",
                        "email": "Lucy1@qq.com",
                        "phone": "15246562356",
                        "question": "喜欢的颜色",
                        "answer": "白色"}
        expresult = "注册成功"
        response = requests.post(url, data=registerinfo).text
        # print(response)
        self.assertIn(expresult, response)

    # 用户登录接口
    def test_case2(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "Lucy1",
                    "password": "123456"}
        expresult = "登录成功"
        response = requests.post(url, data=userinfo).text
        # print(response)
        r = requests.post(url, data=userinfo)
        globals()["session"] = dict(r.cookies)
        # print(globals()["session"])
        self.assertIn(expresult, response)

    # 获取用户信息接口
    def test_case3(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/get_information.do"
        # print(globals()["session"])
        expresult = "data"
        response = requests.post(url, cookies=globals()["session"]).text
        print(response)
        self.assertIn(expresult, response)

    # 更新用户信息接口
    def test_case4(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/update_information.do"
        updateinfo = {"email": "Lucychange@qq.com",
                      "phone": "15246562399",
                      "question": "喜欢的水果",
                      "answer": "芒果"}
        expresult = "更新个人信息成功"
        response = requests.post(url, data=updateinfo, cookies=globals()["session"]).text
        print(response)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(WorkflowUpdateInfo("test_case1"))
    suite.addTest(WorkflowUpdateInfo("test_case2"))
    suite.addTest(WorkflowUpdateInfo("test_case3"))
    suite.addTest(WorkflowUpdateInfo("test_case4"))
    filename = "D:\python\interfaceframe\\testresultfile\mul_interface_report\workflow_update_info1.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="更新个人信息联调接口测试报告")
    runner.run(suite)
