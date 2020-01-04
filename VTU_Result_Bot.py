from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class vtu:
    def login(self, usn):
        self.usn = usn
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.get('https://www.vtu4u.com')
        time.sleep(4)
        btn = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/form/div/div/div[1]/div[2]')  #XPath of CBCS Tab
        btn.click()
        text = bot.find_element_by_xpath('//*[@id="usn"]')  #XPath of usn field
        text.send_keys(usn)
        text.submit()


vish = vtu()
vish.login('Your USN')
