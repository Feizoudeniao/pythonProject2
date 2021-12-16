# 前台购物流程

# 导入类库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
# 海盗商城网址
url='http://192.168.157.128/pirate/index.php?m=user&c=public&a=login'
# 进入海盗商城首页
driver.get(url)
# 输入用户名、密码，点击登录
driver.find_element(By.ID,'username').send_keys('haidao')
driver.find_element(By.ID,'password').send_keys('123456')
# driver.find_element(By.CLASS_NAME,'login_btn').click()
driver.find_element(By.CSS_SELECTOR,'.login_btn.fl').click()

# 点击进入商城购物
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a').click()
driver.find_element(By.LINK_TEXT,'进入商城购物').click()
# 点击商品，进入商品详情页
driver.find_element(By.CLASS_NAME,'lazy').click()
# 获得新窗口句柄
new_window=driver.window_handles[-1]
# 切换到新窗口
driver.switch_to.window(new_window)
# 点击加入购物车
driver.find_element(By.ID,'joinCarButton').click()

# 点击去购物车结算
driver.find_element(By.CLASS_NAME,'shopCar_T_span3').click()
# 点击结算
# driver.find_element(By.CLASS_NAME,'shopCar_btn_03').click()
driver.find_element(By.CSS_SELECTOR,'.shopCar_btn_03.fl').click()
# 点击添加新地址
driver.find_element(By.CLASS_NAME,'add-address').click()
# 收货人
driver.find_element(By.NAME,'address[address_name]').send_keys('小红')
# 手机号
driver.find_element(By.NAME,'address[mobile]').send_keys('13752564562')
# 收货地区
# 省
provice=driver.find_element(By.ID,'add-new-area-select')
Select(provice).select_by_value('610000')
# 市
# city=driver.find_elements(By.CLASS_NAME,'add-new-area-select')[1]
city=driver.find_elements(By.TAG_NAME,'select')[1]
Select(city).select_by_value('610100')
# 区
# region=driver.find_elements(By.CLASS_NAME,'add-new-area-select')[2]
region=driver.find_elements(By.TAG_NAME,'select')[2]
Select(region).select_by_visible_text('雁塔区')
# 详细地址
driver.find_element(By.NAME,'address[address]').send_keys('乐创街区')
# 邮政编码
driver.find_element(By.NAME,'address[zipcode]').send_keys('715400')
# 点击确定
driver.find_element(By.CLASS_NAME,'aui_state_highlight').click()

# 关闭浏览器
driver.quit()