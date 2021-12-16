# 测试驱动程序，包含脚本是否执行及执行顺序
import operator
import unittest
import csv
# from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    filename = "D:\python\interfaceframe\config\config1.csv"
    file = open(filename, "r")
    table = csv.reader(file)
    script_list = []
    script_dict = {}
    i = 0
    for row in table:
        if i > 0:
            # print(row)
            if row[3] == "Yes":
                script_dict = {}
                script_dict[row[1]] = row[0]
                script_dict["num"] = row[4]
                # print(script_dict)
                script_list.append(script_dict)
        i = i + 1
    # print(script_list)
    new_list = sorted(script_list, key=operator.itemgetter("num"))
    # print(new_list)
    line = len(new_list)
    # print(line)
    for i in range(0, line):
        n=0
        for content in new_list[i].items():
            if n==0:
                # print(content)
                fname=content[0]
                fdir=content[1]
                # print("fname:",fname,"\t","fdir:",fdir)
                discover=unittest.defaultTestLoader.discover(fdir,pattern=fname)
                runner=unittest.TextTestRunner()
                # filename="D:\python\interfaceframe\\testresultfile\\frame_report\\runner_v1.html"
                # fp=open(filename,"wb")
                # runner=HTMLTestRunner(stream=fp,title="框架测试报告")
                runner.run(discover)
            n=n+1
    # fp.close()
