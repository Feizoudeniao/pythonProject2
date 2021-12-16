# 接口名称：提交问题答案接口
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/forget_check_answer.do
# 接口参数：1.username 2.question 3.answer
# 接口返回结果：1.forgetToken 2.问题的答案错误

import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestForgetCheckAnswer(unittest.TestCase):
    def test_forget_check_answer(self):
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        filename = p1 + "\\testdatafile\ind_interface\\test_forget_check_answer.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        i = 0
        for row in table:
            if i > 0:
                url = row[0]
                userinfo["username"] = row[1]
                userinfo["question"] = row[2]
                userinfo["answer"] = row[3]
                response = requests.post(url, data=userinfo).text
                self.assertIn(row[4], response)
                dict=eval(response)
                forgetToken=dict["data"]
                return forgetToken
            i = i + 1
        file.close()


if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestForgetCheckAnswer("test_forget_check_answer"))
    filename=r"D:\python\interfaceframe\testresultfile\ind_interface_report\forget_check_answer.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title="提交问题答案接口测试报告")
    runner.run(suite)
    fp.close()

