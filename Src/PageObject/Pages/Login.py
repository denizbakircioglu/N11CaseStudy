import time
from Src.PageObject.Locators import Locator


class ExpectedConditions:
    pass


class Login:
    def goToLogin(self):
        self.driver.get("https://www.n11.com/giris-yap")

    def Login(self):
        #time.sleep(5)
        #self.driver.find_element_by_xpath("//div[@id='dengage-push-perm-slide']/div/div[@class='dn-slide-body']/div[@class='dn-slide-buttons horizontal']/button[@class='dn-slide-deny-btn']").click()
        time.sleep(3)
        self.driver.find_element_by_id("email").send_keys(Locator.login_user)
        self.driver.find_element_by_id("password").send_keys(Locator.login_pass)
        time.sleep(3)
        self.driver.find_element_by_id("loginButton").click()
        time.sleep(5)