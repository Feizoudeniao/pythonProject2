# 注册测试用例
import unittest2
from selenium.webdriver.common.by import By

from func.csvfileManager import reader
from testcase.BaseTestCase import BaseTestCase


class Register3Test(BaseTestCase):
    def test_register3(self):
        table = reader('register.csv')
        for row in table:
            url = 'http://192.168.157.128/pirate/index.php?m=user&c=public&a=reg'
            self.driver.get(url)
            self.driver.find_element(By.NAME, 'username').send_keys(row[0])
            self.driver.find_element(By.NAME, 'password').send_keys(row[1])
            self.driver.find_element(By.NAME, 'userpassword2').send_keys(row[2])
            self.driver.find_element(By.NAME, 'mobile_phone').send_keys(row[3])
            self.driver.find_element(By.NAME, 'email').send_keys(row[4])


if __name__ == '__main__':
    unittest2.main()
