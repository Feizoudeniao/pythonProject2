# 注册测试用例
import unittest2
from selenium.webdriver.common.by import By

from testcase.BaseTestCase import BaseTestCase


class RegisterTest(BaseTestCase):
    def test_register(self):
        url = 'http://192.168.157.128/pirate/index.php?m=user&c=public&a=reg'
        self.driver.get(url)
        self.driver.find_element(By.NAME, 'username').send_keys('张三')
        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        self.driver.find_element(By.NAME, 'userpassword2').send_keys('123456')
        self.driver.find_element(By.NAME, 'mobile_phone').send_keys('13645687895')
        self.driver.find_element(By.NAME, 'email').send_keys('123456@qq.com')


if __name__ == '__main__':
    unittest2.main()
