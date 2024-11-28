#pip install requests beautifulsoup4 #why is it beautifulsoup4 here, where do i downlaod it from if iamusingalocalide
import requests
from bs4 import BeautifulSoup #and bs4 here, also is BeautifulSoup module of package bs4?

url = input("Enter the url of the webpage you want to scrape: ")

response = requests.get(url)
soup = BeautifulSoup(response.content , "html.parser")#woundt it also parse the reponse header, if yes where does it go,also wahat does parse mean,and some other questions as well from chatgpt

headings = soup.find_all("h1")
for heading in headings:
    print(heading.text)
    
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

