from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class twitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/explore')
        time.sleep(5)
        username = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.submit()

    def generate_likes(self, tag):
        time.sleep(6)
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+tag+'&src=typeahead_click')
        time.sleep(10)
        for i in range(1, 50):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(20)
            tweetLinks = [i.get_attribute('href')
                          for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filtered_links = list(filter(lambda x: 'status' in x, tweetLinks))

        for link in filtered_links:
            bot.get(link)
            time.sleep(7)
            try:
                bot.find_element_by_xpath("//div[@data-testid='like']").click()
                time.sleep(7)
            except Exception as ex:
                time.sleep(2)

#input username and password
quincy = twitterBot('<input username>', '<input password>')
quincy.login()
#input required
quincy.generate_likes('<input hashtag or person')

