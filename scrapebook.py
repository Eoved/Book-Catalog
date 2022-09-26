#andrew devoe
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def crawl(isbn):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--log-level=OFF")
        driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        url = "https://www.google.com/search?tbm=bks&q=" + str(isbn)
        #add amazon and https://isbndb.com/ check for book
        driver.get(url)

        #click first result
        results = driver.find_elements_by_xpath("//div[@class='bHexk Tz5Hvf']")
        result = results[0].find_element_by_tag_name("a")
        href = str(result.get_attribute("href"))
        end = href.index('&')
        link = href[:end] + "&hl=en&newbks=1&newbks_redir=1"
        driver.get(link)

        #get book title
        title = driver.find_elements_by_xpath("//div[@class='zNLTKd']")[0].get_attribute('innerText')
        try:
            subtitle = driver.find_elements_by_xpath("//div[@class='Cxh5Uc']")[0].get_attribute('innerText')
            index = subtitle.index(" ·")
            if(index > -1):
                subtitle = subtitle[:index] + ":" + subtitle[index+2:]
            title = title + ": " + subtitle
        except:
            subtitle = ""

        #get author
        author = driver.find_elements_by_xpath("//a[@class='uOHQVb']")[0].get_attribute('innerText')

        driver.close()
        driver.quit()

        return author, title
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        return "error"