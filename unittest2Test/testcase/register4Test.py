# 注册测试用例
import ddt
import unittest2
from selenium.webdriver.common.by import By

from func.csvfileManager import reader
from testcase.BaseTestCase import BaseTestCase


@ddt.ddt
class RegisterTest(BaseTestCase):
    table = reader('register.csv')

    @ddt.data(*table)
    def test_register(self, row):
        url = 'http://192.168.157.128/pirate/index.php?m=user&c=public&a=reg'
        self.driver.get(url)
        self.driver.find_element(By.NAME, 'username').send_keys(row[0])
        self.driver.find_element(By.NAME, 'password').send_keys(row[1])
        self.driver.find_element(By.NAME, 'userpassword2').send_keys(row[2])
        self.driver.find_element(By.NAME, 'mobile_phone').send_keys(row[3])
        self.driver.find_element(By.NAME, 'email').send_keys(row[4])
        # self.driver.find_element(By.CLASS_NAME, 'reg_btn').click()


if __name__ == '__main__':
    unittest2.main()
