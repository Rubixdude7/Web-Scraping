"""
Python3
Nolan Aubuchon
September 17, 2020
Finds the etymology of a given English word using Etymonline.com as a source
enter nothing (press enter twice) to exit the program

I do NOT own Etymonline. All rights to Etymonline go to its respective owner.
"""

from bs4 import BeautifulSoup as bs
import requests

while(True):
	print("Enter a word:\t")
	word = input()
	if(word == ""):
		break
	source = requests.get("https://www.etymonline.com/search?q=" + word).text
	soup = bs(source,"lxml")
	match = soup.find('section')
	try:
		print(match.text)
	except:
		print("entry not found!")
