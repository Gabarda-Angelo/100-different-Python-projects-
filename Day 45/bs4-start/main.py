from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")


yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)



article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)

highest_vote = max(article_upvotes)

highest_votes_index = article_upvotes.index(highest_vote)

print(f"highest votes article upvotes: {article_upvotes[highest_votes_index]}")
print(article_texts[highest_votes_index])
print(article_links[highest_votes_index])








# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
#
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find_all(name="h1", id="name")
# # print(heading)

#you'll get the nearest on the list if you use ".find"
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# class_is_heading = soup.find_all( class_="heading")
# print(class_is_heading)
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# name = soup.select_one("#name")
# print(name)
#
# # soup.select(".heading")
#
# headings = soup.select(".heading")
# print(headings)