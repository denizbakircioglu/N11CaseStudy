import time
from Src.PageObject.Locators import Locator


class ExpectedConditions:
    pass

class Home:
    def goToHome(self):
        self.driver.get("https://www.n11.com")

        current_url = self.driver.current_url

        if current_url == "https://www.n11.com":
            print("Su anda N11 Anasayfada bulunulmaktadir")
        else:
            print("Su anda ", current_url, ".sayfada bulunulmaktadir")