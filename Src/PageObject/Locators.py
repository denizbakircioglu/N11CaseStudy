class Locator(object):
    # Case Study
    login_user = "denizbakircioglu@outlook.com"
    login_pass = "XXXXXXXXX"
    login_submit = "loginButton"
    search_button = "//*[@id='searchData']"
    search_text = "samsung"
    search_submit = "//*[@id=header]/div/div/div[2]/div[1]/div/a/span"
    search_result = "#contentListing > div > div > div.productArea > section.group.listingGroup.resultListGroup.import-search-view > div.header > div.resultText > strong"
    page_number = "//*[@id='contentListing']/div/div/div[2]/div[4]/a[3]"

    product1 = "//div[@id='view']/ul/li[1]/div/div[@class='pro']/span[@title='Favorilere ekle']"
    favorite1 = "//div[@id='view']/ul/li[1]/div/div[@class='pro']/a"
    gofavorite1 = "//div[@id='view']/ul/li[1]/div/div[@class='pro']/a/h3"

    product2 = "//div[@id='view']/ul/li[2]/div/div[@class='pro']/span[@title='Favorilere ekle']"
    favorite2 = "//div[@id='view']/ul/li[2]/div/div[@class='pro']/a"
    gofavorite2 = "//div[@id='view']/ul/li[2]/div/div[@class='pro']/a/h3"

    product3 = "//div[@id='view']/ul/li[3]/div/div[@class='pro']/span[@title='Favorilere ekle']"
    favorite3 = "//div[@id='view']/ul/li[3]/div/div[@class='pro']/a"
    gofavorite3 = "//div[@id='view']/ul/li[3]/div/div[@class='pro']/a/h3"

    istek_listem = "//a[@href='//www.n11.com/hesabim/istek-listelerim']"
    favorilerim = "//div[@class='listItemWrap']/a[@href='https://www.n11.com/hesabim/favorilerim']"