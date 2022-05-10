import requests
from bs4 import BeautifulSoup
from pushover import Pushover

URL = "https://in.bookmyshow.com/sports/tata-indian-premier-league-2022/ET00325171"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

#print(soup.prettify())

div1 = soup.find('div', attrs = {'class':'df-im'}) 

isFinal = False
keyword = "lsg"

for row in div1:
	div2 = row.select('a > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
	text = (div2[0].getText())
	if keyword.casefold() in text.casefold():
		isFinal = True
		break

if isFinal:

	token = "ahaig3kg19ztqi592f34qg9yiahcdv"
	key = "uzxdfxbjcwvngwc176nwihy5jfr245"
	po = Pushover(token)
	po.user(key)
	msg = po.msg("IPL final tickets")
	msg.set("title", "IPL Final Tickets")
	po.send(msg)
	print(isFinal)

