def login_into_nms(self):
    self.driver.get(self.url)
    elem = self.driver.find_element_by_name("login[login]")
    elem.send_keys("admin")
    elem = self.driver.find_element_by_name("login[password]")
    elem.send_keys("12345")
    self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/form/p[3]/button').click()