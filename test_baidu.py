import os
import time
from selenium import webdriver
import unittest
from auto_test.common.config import Config,DRIVER_PATH



class TestBaiDu(unittest.TestCase):
    config = Config()
    url = config.get('URL')


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver.exe')
        self.driver.get(self.url)


    def tearDown(self):
        self.driver.quit()


    def test_search_1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium 灰蓝')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        links = self.driver.find_elements_by_xpath('//*[@id="content_left"]/div/h3/a')
        i = 1
        for link in links:
            print(str(i) + '.' + link.text)
            i += 1


    def test_search_2(self):
        self.driver.find_element_by_id('kw').send_keys('python selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        links = self.driver.find_elements_by_xpath('//*[@id="content_left"]/div/h3/a')
        i = 1
        for link in links:
            print(str(i) + '.' + link.text)
            i += 1


if __name__ == '__main__':
    unittest.main()
