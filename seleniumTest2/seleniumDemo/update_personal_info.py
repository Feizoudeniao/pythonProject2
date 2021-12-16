# 修改个人信息

# 导入类库
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# 海盗商城网址
url='http://192.168.157.128/pirate/index.php?m=user&c=public&a=login'
driver.get(url)
# 输入用户名、密码，点击登录
driver.find_element(By.ID,'username').send_keys('haidao')
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.CSS_SELECTOR,'.login_btn.fl').click()

# 账号设置
driver.find_element(By.LINK_TEXT,'账号设置').click()
# 个人资料
driver.find_element(By.CLASS_NAME,'ico_nav8').click()
# 真实姓名
driver.find_element(By.ID,'true_name').clear()
driver.find_element(By.ID,'true_name').send_keys('海盗三')
# 性别
driver.find_element(By.CSS_SELECTOR,'[value="1"]').click()
# 生日
script='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(script)
driver.find_element(By.ID,'date').clear()
driver.find_element(By.ID,'date').send_keys('1992-02-01')
# QQ
driver.find_element(By.ID,'qq').clear()
driver.find_element(By.ID,'qq').send_keys('1678763221')
# 确认
driver.find_element(By.CLASS_NAME,'btn4').click()

# 弹窗的处理
# sleep(3)
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())
text=driver.switch_to.alert.text
print(text)
driver.switch_to.alert.accept()

# 关闭浏览器
driver.quit()