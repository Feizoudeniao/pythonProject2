# 接口名称：更新用户信息
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/update_information.do
# 接口参数：1.email 2.phone 3.answer 4.question
# 接口返回结果：1.更新个人信息成功 2.email已存在,请更换email再尝试更新 3.更新个人信息失败
import unittest
import requests
import csv
import os

from HTMLTestRunner import HTMLTestRunner


class TestUpdateInfo(unittest.TestCase):
    def setUp(self) -> None:
        url = "http://192.168.157.129:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "Tom",
                    "password": "111111"}
        response = requests.post(url, data=userinfo)
        self.session = dict(response.cookies)

    def test_update_infomation(self):
        path = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        filename = p1 + "\\testdatafile\ind_interface\\test_update_infomation.csv"
        file = open(filename, "r")
        table = csv.reader(file)
        userinfo = {}
        for row in table:
            url = row[1]
            expresult = row[3]
            j = int(row[6])
            for i in range(7, 2 * j + 7, 2):
                userinfo[row[i]] = row[i + 1]
            # print(userinfo)
            response=requests.post(url,data=userinfo,cookies=self.session).text
            self.assertIn(row[3],response)
            userinfo = {}
        file.close()


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestUpdateInfo("test_update_infomation"))
    filename = "D:\python\interfaceframe\\testresultfile\ind_interface_report\\update_infomation.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="更新用户信息测试报告")
    runner.run(suite)
    fp.close()
