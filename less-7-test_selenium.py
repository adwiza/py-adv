from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver


class MainPage(Page):
    page_url = "https://mail.ru"

    def auth(self):
        try:
            login_field = self.webdriver.find_element_by_id('mailbox__login')
            password_field = self.webdriver.find_element_by_id('mailbox__password')
            auth_button = self.webdriver.find_element_by_id('mailbox__auth__button')

        except NoSuchElementException:
            return
        login_field.send_keys(conf.mail.login)
        password_field.send_keys(conf.mail.password)
        try:
            auth_button.click()
        except:
            pass
