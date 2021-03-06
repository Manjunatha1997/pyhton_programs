import requests
from bs4 import BeautifulSoup


# url = 'https://www.amazon.com/s?k=boat+headset+bluetooth+wireless&crid=2RTQZNJUQ6D9&sprefix=boat+headset%2Caps%2C371&ref=nb_sb_ss_ts-doa-p_2_12'
url = 'https://www.amazon.com/'

r = requests.get(url)
web_page = BeautifulSoup(r.content)

images = web_page.find_all('p')
print(images)
print('*******************************')
print(images[0])



