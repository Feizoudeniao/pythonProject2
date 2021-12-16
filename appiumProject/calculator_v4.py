# V4.0实现计算器多组任意数的组合运算测试
import csv

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

# 定义一个字典，存放参数设置
caps={}
caps['automatorName']='UiAutomator2'
caps['platformName']='Android'
caps['platformVersion']='6.0'
caps['deviceName']='192.168.140.101:5555'
caps['appPackage']='com.android.calculator2'
caps['appActivity']='.Calculator'

driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)


file=open('testdata2.csv','r')
table=csv.reader(file)
for row in table:
    x=row[0]+row[1]+row[2]+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]
    expresult=row[9]
    driver.find_element(By.ID,'com.android.calculator2:id/formula').send_keys(x)
    driver.find_element(By.ID,'com.android.calculator2:id/eq').click()
    result=driver.find_element(By.ID,'com.android.calculator2:id/formula').text
    if result==expresult:
        print("测试通过")
    else:
        print("测试失败")
    el=driver.find_element(By.ID,'com.android.calculator2:id/clr')
    # TouchActions(driver).long_press(el).perform()
    TouchAction(driver).long_press(el).perform().wait(3000)
    driver.find_element(By.ID,'com.android.calculator2:id/clr').click()
file.close()
