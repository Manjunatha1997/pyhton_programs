
from bs4 import BeautifulSoup
import requests


fr = open('ddddddddddd.txt')

data = fr.readlines()

for url in data:
	url = url.strip()
	print(url)

	r = requests.get(url)

	web_page = BeautifulSoup(r.content,features="lxml")

	code = web_page.find_all('td',attrs={'class':'code'})


	for i in code:
		print('###########################################################################')
		fa = open('code.txt','a')
		print(i.text)
		fa.write(i.text+'\n')
		fa.close()
		print('***************************************************************************')


fr.close()


