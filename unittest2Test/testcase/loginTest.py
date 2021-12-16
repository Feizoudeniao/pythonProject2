# 登录测试用例
import unittest2
from selenium.webdriver.common.by import By

from testcase.BaseTestCase import BaseTestCase


class LoginTest(BaseTestCase):
    def test_login(self):
        self.driver.get('http://192.168.157.128/pirate/index.php?m=user&c=public&a=login')
        self.driver.find_element(By.ID, 'username').send_keys('haidao')
        self.driver.find_element(By.ID, 'password').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, 'login_btn').click()
        # self.assertEquals('')
        # print(self.driver.title)
        # print(self.driver.current_url)
        self.assertEquals('http://192.168.157.128/pirate/index.php?m=user&c=public&a=login',self.driver.current_url)


if __name__ == '__main__':
        unittest2.main()