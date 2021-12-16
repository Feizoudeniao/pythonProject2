# v1.0 安装卸载测试

# 导入类库
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

# 定义一个字典，存放参数设置
caps = {}
caps['automationName'] = 'UiAutomator2'
caps['platformName'] = 'Android'
caps['platVersion'] = '6.0'
caps['deviceName'] = '192.168.140.101:5555'
caps['appPackage'] = 'com.android.launcher3'
caps['appActivity'] = '.Launcher t92'

driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
# 卸载APP
driver.remove_app('com.youdao.note')
# 安装APP
driver.install_app('D:\python\youdaoyunbiji_84.apk')

# 1.安装后用程序启动有道云
caps['appPackage']='com.youdao.note'
caps['appActivity']='.activity2.MainActivity t101'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)

time.sleep(3)
# 2.弹出界面上抓取'拒绝'连接
el=driver.find_element(By.ID,'com.android.packageinstaller:id/permission_deny_button').is_enabled()
print(el)
# 3.如果链接存在的，那么打印安装成功
# 4.否则，打印安装失败
if el:
    print('安装成功')
else:
    print('安装失败')

# # 2.1 弹出界面上抓取“有道云笔记”
# el=driver.find_element(By.ID,'com.android.packageinstaller:id/permission_message').text
# msg=el.find('有道云笔记')
# if msg>0:
#     print('安装成功')
# else:
#     print('安装失败')
driver.quit()
