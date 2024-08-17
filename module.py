import requests
from selenium import webdriver

class WebInteractionModule:
    def __init__(self):
        self.session = requests.Session()
        self.driver = webdriver.Chrome()  # 或者使用其他浏览器驱动

    def interact(self, action: Dict) -> str:
        if action['type'] == 'get':
            return self.session.get(action['url']).text
        elif action['type'] == 'click':
            element = self.driver.find_element_by_xpath(action['xpath'])
            element.click()
            return self.driver.page_source
        # 添加更多交互类型...

    def close(self):
        self.driver.quit()