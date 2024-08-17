from bs4 import BeautifulSoup
import json
import os
from model import query_llm
from typing import Dict
class DataExtractor:
    def extract(self, html: str) -> Dict:
        soup = BeautifulSoup(html, 'html.parser')
        # 使用LLM来动态生成提取规则
        extraction_rules = self._generate_extraction_rules(soup.prettify())
        return self._apply_extraction_rules(soup, extraction_rules)

    def _generate_extraction_rules(self, html_sample: str) -> Dict:
        prompt = f"Given this HTML sample, generate extraction rules for order details:\n{html_sample}\nProvide a structured response with XPath or CSS selectors for each field."
        return eval(query_llm(prompt))

    def _apply_extraction_rules(self, soup: BeautifulSoup, rules: Dict) -> Dict:
        extracted_data = {}
        for field, selector in rules.items():
            extracted_data[field] = soup.select_one(selector).text.strip()
        return extracted_data



class DataStorage:
    def __init__(self, base_path: str = 'order_data'):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def store(self, data: Dict):
        order_id = data.get('order_id', 'unknown')
        file_path = os.path.join(self.base_path, f'order_{order_id}.json')
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)