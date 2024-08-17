import requests
from typing import Dict
from bs4 import BeautifulSoup
from model import query_llm
import re

class ActionExecutor:
    def execute(self, action: Dict) -> Dict:
        if action['action'] == 'login':
            return self._login()
        elif action['action'] == 'navigate_to_orders':
            return self._navigate_to_orders()
        elif action['action'] == 'extract_order_details':
            return self._extract_order_details()
        # 添加更多动作...

    def _login(self,username,password) -> Dict:
        self.session = requests.Session()
        login_url = "https://www.amazon.com/ap/signin"

        payload = {
            "email": username,
            "password": password
        }

        response = self.session.post(login_url, data=payload)

        if response.status_code == 200:
            print("Authentication successful")
            return self.session
        else:
            print("Authentication failed")
            return None

    def _navigate_to_order_details(session):
        orders_url = "https://www.amazon.com/gp/your-account/order-history"
        response = session.get(orders_url)

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取所有可能的订单链接
        potential_links = [a['href'] for a in soup.find_all('a', href=True) if 'order-details' in a['href']]

        # 使用LLM分析页面内容并决定下一步操作
        prompt = f"""
        Analyze the following list of potential order detail links:
        {potential_links}

        1. Are these links valid order detail links?
        2. If yes, return these links as a Python list.
        3. If no, explain why they are not valid and suggest how to find the correct links.

        Provide your response in the following format:
        VALID: [True/False]
        LINKS: [list of links or empty list]
        EXPLANATION: Your explanation here
        """

        llm_response = query_llm(prompt)

        # 解析LLM的响应
        valid = re.search(r'VALID: (True|False)', llm_response).group(1) == 'True'
        links = eval(re.search(r'LINKS: (\[.*?\])', llm_response, re.DOTALL).group(1))
        explanation = re.search(r'EXPLANATION: (.*)', llm_response, re.DOTALL).group(1).strip()

        if valid and links:
            return links
        else:
            print(f"Unable to find valid order detail links. LLM explanation: {explanation}")
            return []

    def _extract_order_details(order_html):
        soup = BeautifulSoup(order_html, 'html.parser')
        # 解析订单详情，如订单号，产品名称，数量，价格，交付状态等
        order_details = {}
        # 示例提取
        order_details['order_number'] = soup.find('span', {'id': 'orderNumber'}).text
        # 继续提取其他数据
        return order_details