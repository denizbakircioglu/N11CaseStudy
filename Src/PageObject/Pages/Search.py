import time
from selenium.webdriver import Keys
from Src.PageObject.Locators import Locator


class ExpectedConditions:
    pass


class Search:

    def Search(self):
        search_box = self.driver.find_element_by_id("searchData")
        search_box.send_keys("samsung")
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

    def SearchResultControlgo2Page(self):
        search_result_count = self.driver.find_element_by_css_selector(Locator.search_result)
        count = float(search_result_count.text)
        if count > 0:
            print(count, " Adet urun bulunmustur.")
            self.driver.get("https://www.n11.com/arama?q=samsung&pg=2")
            time.sleep(5)
            page = self.driver.find_element_by_xpath(Locator.page_number)
            page_number = int(page.text)
            if page_number == 2:
                print("Su anda 2.sayfada bulunulmaktadir")
            else:
                print("Su anda ", page_number, ".sayfada bulunulmaktadir")
        else:
            print("Arama sonucunda herhangi bir urun bulunamamistir.")
