# 接口名称：获取用户信息
# 接口请求方法：post
# 接口请求地址：http://192.168.157.129:8080/jwshoplogin/user/get_information.do
# 接口参数：
# 接口返回结果：1.显示用户信息 2.找不到当前用户
import unittest
import requests

from HTMLTestRunner import HTMLTestRunner


class TestGetInfo(unittest.TestCase):
    def setUp(self) -> None:
        url = "http://192.168.157.129:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "Tom",
                    "password": "111111"}
        response = requests.post(url, data=userinfo)
        self.session = dict(response.cookies)

    def test_get_information(self):
        url = "http://192.168.157.129:8080/jwshoplogin/user/get_information.do"
        response = requests.post(url, cookies=self.session).text
        self.assertIn("Tom", response)


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestGetInfo("test_get_information"))
    filename = "D:\python\interfaceframe\\testresultfile\ind_interface_report\\get_infomation.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="获取用户信息测试报告")
    runner.run(suite)
    fp.close()
