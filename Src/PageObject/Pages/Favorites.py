import time
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class ExpectedConditions:
    pass

class Favorites:
    favorite1 = ""
    favorite2 = ""
    favorite3 = ""

    def AddFavorite3Product(self):
        self.driver.find_element_by_xpath().click(Locator.product1)
        self.favorite1 = self.driver.find_element_by_xpath(Locator.favorite1).get_attribute("title")
        self.driver.find_element_by_xpath(Locator.product2).click()
        self.favorite2 = self.driver.find_element_by_xpath(Locator.favorite2).get_attribute("title")
        self.driver.find_element_by_xpath(Locator.product3).click()
        self.favorite3 = self.driver.find_element_by_xpath(Locator.favorite3).get_attribute("title")

    def goToFavorites(self):
        self.driver.find_element_by_xpath(Locator.istek_listem)
        self.driver.find_element_by_xpath(Locator.favorilerim)
        if self.favorite1 == self.driver.find_element_by_xpath(Locator.gofavorite1).text:
            print("1. izlemeye alinan urun favorilerde bulunmaktadir.")
        else:
            print("1. izlemeye alinan urun favorilerde bulunmamaktadir.")
        if self.favorite2 == self.driver.find_element_by_xpath(Locator.gofavorite2).text:
            print("2. izlemeye alinan urun favorilerde bulunmaktadir.")
        else:
            print("2. izlemeye alinan urun favorilerde bulunmamaktadir.")
        if self.favorite3 == self.driver.find_element_by_xpath(Locator.gofavorite3).text:
            print("3. izlemeye alinan urun favorilerde bulunmaktadir.")
        else:
            print("3. izlemeye alinan urun favorilerde bulunmamaktadir.")

    def DeleteFavoriteProduct(self):
        favorites = self.driver.find_elements(By.XPATH, "//div[@class='wishProBtns']/span")
        for item in favorites:
            item.click()
            self.driver.find_element_by_xpath("//span[text()='Tamam']").click()
            time.sleep(2)
        favorite = self.driver.find_element_by_xpath("//div[text()='İzlediğiniz bir ürün bulunmamaktadır.']")
        l = len(favorite)
        if l > 0:
            print("izlemeye alinan urunler silinemedi")
        else:
            print("izlemeye alinan urunler kaldirildi")