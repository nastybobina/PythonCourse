import requests
import re


def data_in_json(url):
    response = requests.get(url)
    return response.text


def extract_subheadings(html_content):
    pattern = re.compile(r'<h3.*?>(.*?)<\/h3>', re.DOTALL)
    matches = pattern.findall(html_content)
    return [re.sub(r'<.*?>', '', match).strip() for match in matches]


target_url = "http://www.columbia.edu/~fdc/sample.html"  # URL нашей страницы
html_content = data_in_json(target_url)
subheadings = extract_subheadings(html_content)
print(subheadings)
