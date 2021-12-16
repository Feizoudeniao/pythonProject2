# 注册测试用例
import csv

import unittest2
from selenium.webdriver.common.by import By

from testcase.BaseTestCase import BaseTestCase


class Register2Test(BaseTestCase):
    def test_register2(self):
        filename = r'D:\python\unittest2Test\testdata\register.csv'
        file = open(filename, 'r')
        table = csv.reader(file)
        for row in table:
            i = 0
            if i == 0:
                pass
            else:
                # url = 'http://192.168.157.128/pirate/index.php?m=user&c=public&a=reg'
                # self.driver.get(url)
                # self.driver.find_element(By.NAME, 'username').send_keys(row[0])
                # self.driver.find_element(By.NAME, 'password').send_keys(row[1])
                # self.driver.find_element(By.NAME, 'userpassword2').send_keys(row[2])
                # self.driver.find_element(By.NAME, 'mobile_phone').send_keys(row[3])
                # self.driver.find_element(By.NAME, 'email').send_keys(row[4])
                print(row)
            i = i + 1
        file.close()


if __name__ == '__main__':
    unittest2.main()
