# 添加商品
# 导包
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

# 打开浏览器
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

url = 'http://192.168.157.128/pirate/index.php?m=admin&c=public&a=login'
driver.get(url)

# 输入用户名、密码、验证码点击登录
driver.find_element(By.NAME, 'username').send_keys('admin')
driver.find_element(By.NAME, 'userpass').send_keys('password')
driver.find_element(By.NAME, 'userverify').send_keys('1234')
driver.find_element(By.CLASS_NAME, 'Btn').click()

# 商品管理
driver.find_element(By.LINK_TEXT, '商品管理').click()
# 添加商品
driver.find_element(By.CSS_SELECTOR, '.n11.z_side').click()
# 切换frame
frame = driver.find_element(By.ID, 'mainFrame')
driver.switch_to.frame(frame)
# 商品名称
driver.find_element(By.NAME, 'name').send_keys('iphone xs max')
# 商品分类
driver.find_element(By.ID, '1').click()
driver.find_element(By.ID, '2').click()
driver.find_element(By.ID, '3').click()
ele = driver.find_element(By.ID, '4')
ActionChains(driver).double_click(ele).perform()

# 商品品牌
brand = driver.find_element(By.NAME, 'brand_id')
Select(brand).select_by_value('2')
# 商品图册
driver.find_element(By.CSS_SELECTOR,'body > div.content > div.install.tabs.mt10 > dl > dt > a:nth-child(5)').click()
# 点击选择图片
driver.find_element(By.NAME,'file').send_keys(r'C:\Users\Administrator\Desktop\DB测试.png')
# 开始上传
driver.find_element(By.CSS_SELECTOR,'.uploadBtn.state-finish.state-ready').click()
# 处理弹窗
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())
text=driver.switch_to.alert.text
print(text)
driver.switch_to.alert.accept()
# 提交
driver.find_element(By.CLASS_NAME,'button_search').click()
driver.quit()


