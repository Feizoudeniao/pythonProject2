# 接口名称：回答完密保问题后修改密码
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/forget_reset_password.do
# 接口参数：1.username 2.passwordNew 3.forgetToken
# 接口返回结果：1.修改密码成功 2.参数错误,token需要传递 3.用户不存在
# 4.token无效或者过期 5.token错误,请重新获取重置密码的token 6.修改密码失败

import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


# from script.ind_interface.test_forget_check_answer import TestForgetCheckAnswer


class TestForgetResetPassword(unittest.TestCase):
    def setUp(self) -> None:
        url="http://192.168.157.129:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo = {"username":"Tom",
                    "question":"喜欢吃的菜",
                    "answer":"西蓝花"}
        response = requests.post(url, data=userinfo).json()
        self.forgetToken=response["data"]
        print(self.forgetToken)

    def test_forget_reset_password(self):
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        filename = p1 + "\\testdatafile\ind_interface\\test_forget_reset_password.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i == 1:
                url = row[0]
                userinfo["username"] = row[1]
                userinfo["passwordNew"] = row[2]
                userinfo["forgetToken"] = self.forgetToken
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[3], response)
            if i == 2:
                url = row[0]
                userinfo["username"] = row[1]
                userinfo["passwordNew"] = row[2]
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[3], response)
            i = i + 1
        file.close()


if __name__ == '__main__':
    # checkanswerObj = TestForgetCheckAnswer()
    # forgetToken = checkanswerObj.test_forget_check_answer()
    # resetpasswordObj= TestForgetResetPassword()
    # resetpasswordObj.test_forget_reset_password(forgetToken)

    suite = unittest.TestSuite()
    suite.addTest(TestForgetResetPassword("test_forget_reset_password"))
    filename = r"D:\python\interfaceframe\testresultfile\ind_interface_report\forget_reset_password.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="回答完密保问题后修改密码测试报告")
    runner.run(suite)
    fp.close()
