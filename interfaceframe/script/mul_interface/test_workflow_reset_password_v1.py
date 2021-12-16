# 接口联调测试 共涉及五个测试方法，接口如下：
# 1.用户注册接口
# 2.用户登录接口
# 3.忘记密码提示密保接口
# 4.提交问题答案接口
# 5.回答完密保问题后修改密码

import unittest
import requests

from HTMLTestRunner import HTMLTestRunner


class WorkflowResetPwd(unittest.TestCase):
    def test_case1(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/register.do"
        userinfo = {"username": "Alex7",
                    "password": "123456",
                    "email": "alex7@qq.com",
                    "phone": "15246562356",
                    "question": "喜欢的颜色",
                    "answer": "白色"}
        response = requests.post(url, data=userinfo).text
        self.assertIn("注册成功", response)

    def test_case2(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "Alex7",
                    "password": "123456"}
        response = requests.post(url, data=userinfo).text
        self.assertIn("登录成功", response)

    def test_case3(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/forget_get_question.do"
        userinfo = {"username": "Alex7"}
        response = requests.post(url, data=userinfo).text
        self.assertIn("喜欢的颜色", response)

    def test_case4(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo = {"username": "Alex7",
                    "question": "喜欢的颜色",
                    "answer": "白色"}
        response = requests.post(url, data=userinfo).text
        dic = eval(response)
        globals()['token'] = dic["data"]
        print(globals()['token'])
        self.assertIn("data", response)

    def test_case5(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo = {"username": "Alex7",
                    "passwordNew": "111111",
                    "forgetToken": globals()['token']}
        print(userinfo)
        response = requests.post(url, data=userinfo).text
        self.assertIn("修改密码成功", response)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(WorkflowResetPwd("test_case1"))
    suite.addTest(WorkflowResetPwd("test_case2"))
    suite.addTest(WorkflowResetPwd("test_case3"))
    suite.addTest(WorkflowResetPwd("test_case4"))
    suite.addTest(WorkflowResetPwd("test_case5"))
    suite.addTest(WorkflowResetPwd("test_case2"))
    filename = "D:\python\interfaceframe\\testresultfile\mul_interface_report\workflow_reset_passwd1.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="回答完密保问题后修改密码测试报告")
    runner.run(suite)
    fp.close()
