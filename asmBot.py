from selenium import webdriver
from time import sleep

class asmBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setsite(self):
         self.driver.get('https://msa.magister.net/')

    def setusername(self):
        user_inp = self.driver.find_element_by_xpath('//*[@id="username"]')
        user_inp.send_keys('diep22534')    

        doorgaan_btn = self.driver.find_element_by_xpath('//*[@id="username_submit"]')
        doorgaan_btn.click()

    def setpassword(self):
        password_inp = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_inp.send_keys('niggercmd')

    def pressbutton(self):
        login_btn = self.driver.find_element_by_xpath('//*[@id="password_submit"]')
        login_btn.click()

bot = asmBot()
bot.setsite()

sleep(2)
bot.setusername()

sleep(0.5)
bot.setpassword()

bot.pressbutton()
sleep(0.1)
bot.pressbutton()
sleep(0.1)
bot.pressbutton()
sleep(0.1)
bot.pressbutton()
sleep(0.1)
bot.pressbutton()
