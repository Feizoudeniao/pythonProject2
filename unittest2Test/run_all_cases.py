# 组织执行测试用例
import unittest2

from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 找到需要执行的测试用例
    suite = unittest2.defaultTestLoader.discover('./testcase', '*Test.py')
    # # 执行找到的测试用例
    # unittest2.TextTestRunner().run(suite)
    # 生成测试报告
    path='report/registerReport.html'
    file=open(path,'wb')
    HTMLTestRunner(stream=file,verbosity=1,title='注册测试报告').run(suite)
