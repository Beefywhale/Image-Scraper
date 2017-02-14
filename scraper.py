import urllib
import urllib.request
import os

if not os.path.exists('imgs'):
    os.makedirs('imgs')

def scrape():
	'''Scrape for images!'''
	url_i = input('Url to get images from: ')
	try:
		gr = urllib.request.urlopen(url_i)
	except ValueError:
		print('Wrong url format! make sure your url starts with "http" or "https"!')
		exit()
	try: 
		from BeautifulSoup import BeautifulSoup
	except ImportError:
		from bs4 import BeautifulSoup
		html = gr.read()
		results = []
		parsed_html = BeautifulSoup(html, "html.parser")
		num = 0
		for item in parsed_html.find_all('img'):
			img_num = len(parsed_html.find_all('img'))
			try:
				urllib.request.urlretrieve(url_i+item['src'], 'imgs/img{}.jpg'.format(num))
				print('Downloading image {} of {}!'.format(num, img_num))
			except:
				urllib.request.urlretrieve(item['src'], 'imgs/img{}.jpg'.format(num))
				print('Downloading image {} of {}!'.format(num, img_num))
			num += 1
		print('Finished! Downloaded {} images!'.format(img_num))
scrape()