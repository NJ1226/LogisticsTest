from selenium import webdriver
import selenium,os,logging,datetime,HTMLTestRunner,BeautifulReport,traceback


# 记录错误日志
def Log(message):
    now_date = datetime.datetime.now().strftime('%Y%m%d')
    now_datetime = datetime.datetime.now()
    filepath = "../Log/"
    full_path = filepath + 'Log_' + now_date + '.txt'
    file = open(full_path, 'a+')
    file.write(str(now_datetime) + ':' + message + '\n')

# 登陆系统
def Logon(driver):
    try:
        username = 'aa'
        password = 'bb'
        url = "cc"
        driver.get(url)
        driver.find_element_by_id("txtUserName").send_keys(username) # 输入用户名
        driver.find_element_by_id("txtPassword").send_keys(password) # 输入密码
        driver.find_element_by_id("btnSubmit").click() # 点击登陆按钮
    except BaseException as e:
        message = str(e)
        line = str(traceback.print_exc())
        Log('错误行数：' + line + message)

# 获取物流中心添加元素位置
def bb(driver):
    try:
        L = range(50)
        for i in L:
            if driver.find_element_by_xpath("//*[@id='LogisticsStation']/div[" + str(i+1) + "]").is_displayed() == True:
                i = i + 1
            else:
                i = i - 1
                return i
    except BaseException as e:
        return i

# 成成测试报告
def TestReport1(test_suit):
    now_date = datetime.datetime.now().strftime('%Y%m%d')
    filepath = "../TestReport/"
    full_path = filepath + 'Report_' + now_date + '.html'
    file = open(full_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='自动化测试报告', description='执行情况')
    #   生成执行用例的对象
    runner.run(test_suit)
    # result = BeautifulReport(test_suit)
    # result.report(filename= 'report.html',description='测试报告',log_path='TestReport')

def TestReport2(test_suit):
    filepath = '../TestReport/'
    now = datetime.datetime.now().strftime('%Y%m%d')
    name = 'Report_' + str(now) + '.html'
    fullpath = filepath + name
    file = open(fullpath, 'wb')
    result = BeautifulReport.BeautifulReport(test_suit)
    result.report(filename=name, description='物流中心管理—添加', log_path=filepath)

# 判断元素是否存在，存在返回True，不存在返回False
def IsElementExist(driver,element):
    flag = True
    try:
        driver.find_element_by_xpath(element).is_displayed()
        return flag
    except:
        flag = False
        return flag




