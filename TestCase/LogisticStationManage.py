# -*- coding: UTF-8 -*-
import selenium,time,unittest,traceback
from selenium import webdriver
from selenium.webdriver.support.select import Select
from TestCase.PublicMethod import Logon,bb,IsElementExist


class MyTest(unittest.TestCase):
    def test_物流中心管理_添加(self):
        '''物流中心管理_添加功能'''
        print('222')
        try:
            driver = webdriver.Chrome()
            Logon(driver)
            time.sleep(20)
            element1 = driver.find_element_by_xpath("//*[@id='superMenus']/li[1]")
            driver.execute_script("arguments[0].click();", element1)
            element2 = driver.find_element_by_xpath("//span[contains(text(),'物流中心管理')]")
            driver.execute_script("arguments[0].click();", element2)
            time.sleep(2)
            driver.switch_to.frame(1)
            Num = bb(driver)
            driver.find_element_by_xpath("//*[@id='LogisticsStation']/div[" + str(Num) + "]").click()
            driver.switch_to.frame("frame")
            logisticstationname = "自动化物流"
            driver.find_element_by_id("StationName").send_keys(logisticstationname)
            driver.find_element_by_id("ContainsWareHouse").send_keys(u"上海仓库")
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/label").click()
            time.sleep(2)
            Select(driver.find_element_by_xpath("//*[@id='Province']")).select_by_visible_text("上海市")
            Select(driver.find_element_by_xpath("//*[@id='City']")).select_by_visible_text("上海市")
            time.sleep(2)
            Select(driver.find_element_by_xpath("//*[@id='District']")).select_by_visible_text("闵行区")
            driver.find_element_by_xpath("//*[@id='Address']").send_keys(u"东方明珠")
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='btnSave']").click()
            elemennt = "//label[contains(text()," + "'" + logisticstationname + "'" + ")]"
            flag = IsElementExist(driver,elemennt)
            self.assertEqual(flag,True,msg='物流中心创建失败')
            driver.quit()
        except BaseException as e:
            print(str(e))
            raise e















