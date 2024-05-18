import requests
from bs4 import BeautifulSoup

with open("data\zample.html", "r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div")[1])

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# s = soup.find(id="link3")
# print(s.get("href"))
    
# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))
# print(soup.find(class_="italic"))

#==========  Get all children of any parent =================

# for child in soup.find(class_="container").children:
#     print(child)

# ============== get all parent of any elements ==============

# for parent in soup.find(class_="box").parents:
#     print(parent)

# =============== Modify content ========================

# cont = soup.find(class_="container")
# cont.name = "span"
# cont["class"] = "my class"
# cont.string = "I am a strings"
# print(cont)

#  =============== Insert New Tags =======================

# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Contact"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)
# with open("Modified.html", 'w') as f:
#     f.write(str(soup))

# ============ check that atrribute is avialble or not ===========


# cont = soup.find(class_="container")
# print(cont.has_attr("class"))

# =================== write functions ========================

# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

