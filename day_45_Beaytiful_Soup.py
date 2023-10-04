from bs4 import BeautifulSoup
import lxml
import requests

# with open("day_45_Beaytiful_Soup.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# # print(soup.title.string)
# # print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="name")
# # print(section_heading.getText())

# # company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

print(soup.title)













