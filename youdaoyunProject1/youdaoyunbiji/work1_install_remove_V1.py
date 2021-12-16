# 用面向对象的思想实现安装卸载的自动化测试

# 导入类库
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


# 定义测试安装卸载类
class YdInstallRemove():
    # 初始化方法
    def __init__(self):
        # 加self为属性
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '6.0'
        self.caps['deviceName'] = '192.168.140.101:5555'
        self.caps['appPackage'] = 'com.android.launcher3'
        self.caps['appActivity'] = '.Launcher t92'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    # 安装卸载方法
    def test_install_remove(self):
        self.driver.remove_app('com.youdao.note')
        self.driver.install_app('D:\python\youdaoyunbiji_84.apk')

    # 检查安装方法
    def check_install(self):
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity t101'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        el = self.driver.find_element(By.ID, 'com.android.packageinstaller:id/permission_deny_button').is_enabled()
        if el:
            print('安装成功')
        else:
            print('安装失败')
        self.driver.quit()


if __name__ == '__main__':
    # 把类实例化为对象  初始化类的对象
    ydObj = YdInstallRemove()
    # 调用安装卸载方法
    ydObj.test_install_remove()
    # 调用检查安装方法
    ydObj.check_install()
