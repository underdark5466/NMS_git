from login_into_nms import login_into_nms
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Network_tabs_test:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def get_graph_source_tab(self):
        self.driver.get(self.url + '#/net_graph/?net_id=1')
        found = False
        while not found:
            try:
                self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/div[1]/select/option[1]')
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/div[1]/select/option[2]')
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/div[1]/select/option[3]')
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/div[1]/select/option[4]')
                found = True
            except NoSuchElementException:
                sleep(1)
                print("One of graphs doesn't exist.")


lol = Network_tabs_test('http://10.0.3.52')
login_into_nms(lol)

# lol.get_graph_source_tab()


