# V5.0负号的处理

# 导入appium类库
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

# 定义一个字典，存放参数设置


caps = {}
# 测试框架
caps["automationName"] = "UiAutomator2"

# 设置模拟器参数
# 操作系统
caps['platformName'] = 'Android'
# 操作系统版本
caps['platformVersion'] = '6.0'
caps['deviceName'] = '192.168.140.101:5555'

# 设置被测程序参数
caps['appPackage'] = 'com.android.calculator2'
caps['appActivity'] = '.Calculator'

driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)

driver.find_element(By.ID, 'com.android.calculator2:id/digit_5').click()
driver.find_element(By.ID, 'com.android.calculator2:id/op_sub').click()
driver.find_element(By.ID, 'com.android.calculator2:id/digit_8').click()
driver.find_element(By.ID, 'com.android.calculator2:id/eq').click()

result = driver.find_element(By.ID, 'com.android.calculator2:id/formula').text
print(result)

if result[0]=='−':
    result=result.replace('−','-')
    print(result)
# 比对结果
if int(result)==-3:
    print("测试通过")
else:
    print("测试失败")