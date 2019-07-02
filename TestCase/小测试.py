import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime,os,time,logging,unittest,traceback,BeautifulReport
from TestCase.PublicMethod import Log,Logon,IsElementExist
import TestCase.LogisticStationManage



try:
    driver = webdriver.Chrome()
    Logon(driver)
    title = driver.title
    url = driver.current_url
    element1 = driver.find_element_by_xpath("//*[@id='superMenus']/li[1]")
    driver.execute_script("arguments[0].click();", element1)
    element2 = driver.find_element_by_xpath("//span[contains(text(),'物流中心管理')]")
    driver.execute_script("arguments[0].click();", element2)
    time.sleep(2)
    driver.switch_to.frame(1)
    #  self.assertEqual(flag, True, msg='物流中心创建失败')
    logisticstationname = "自动化物流"
    elemennt = "//label[contains(text()," + "'"+logisticstationname+"'"+ ")]"
    flag2 = IsElementExist(driver, elemennt)
    print(flag2)
except BaseException as e:
    message = str(e)
    message = '错误行数：' + traceback.format_exc() + '\n错误信息：' + message
    Log(message)



