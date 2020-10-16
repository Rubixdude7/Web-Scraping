"""
Python3
Nolan Aubuchon
October 14, 2020
Inputs a given English definition and outputs cognates in the Uralic language family (i.e. fire, water) using the Uralonet database

I do NOT own Uralonet. All rights to Uralonet go to its respective owner.
"""


codes = {"hun":"Hungarian",
"kca":"Khanty",
"mns":"Mansi",
"est":"Estonian",
"ekk":"Estonian",
"fin":"Finnish",
"fkv":"Kven",
"fit":"Tornedalen",
"izh":"Ingrian",
"krl":"Karelian",
"liv":"Liv",
"olo":"Livvi-Karelian",
"lud":"Ludian",
"vep":"Veps",
"vot":"Vod",
"vro":"Võro",
"mrj":"Hill Mari",
"mhr":"Meadow Mari",
"myv":"Erzya",
"mdf":"Moksha",
"udm":"Udmurt",
"koi":"Komi-Permyak",
"kpv":"Komi-Zyrian",
"sia":"Akkala Saami",
"smn":"Inari Saami",
"sjd":"Kildin Saami",
"sms":"Skolt Saami",
"sjt":"Ter Saami",
"sju":"Ume Saami",
"smj":"Lule Saami",
"sme":"North Saami",
"sje":"Pite Saami",
"sma":"South Saami",
"yrk":"Nenets",
"nio":"Nganasan",
"enf":"Forest Enets",
"enh":"Tundra Enets",
"xas":"Kamas",
"sel":"Selkup"}

url = "http://uralonet.nytud.hu/search.cgi?locale=en_GB&submit=Search&rkn_BED_l=en&rkn_l=%25&rkn_BED=fire&rkn_c=1" #example word: fire
url_a = "http://uralonet.nytud.hu/search.cgi?locale=en_GB&submit=Search&rkn_BED_l=en&rkn_l=%25&rkn_BED="
url_a_1 = "http://uralonet.nytud.hu/"
url_b = "&rkn_c=1"

from bs4 import BeautifulSoup as bs
import requests

while(True):
	mylemmas = []
	entries = []
	print("Enter a word:\t")
	word = input()
	if(word == ""):
		break
	
	
	source = requests.get(url_a + word + url_b).text
	soup = bs(source,"lxml-xml")
	matches = soup.find_all('a',class_ = "l")
	for lemma in matches:
		l = lemma.find_all("span",{"class":"bed","xml:lang":"en"})
		for e in l:
			if (e.text.rstrip() == word):
				mylemmas.append(lemma)
	try:
		if(len(mylemmas) == 0):
			raise KeyError
		for e in mylemmas:
			entries.append(e['href'])
	except:
		print("Entry not valid!")
	else:
		for e in entries:
			source2 = requests.get(url_a_1 + e + "&locale=en_GB").text
			soup2 = bs(source2,"lxml-xml")
			#
			protoform = soup2.find('span',{"class":"ural5","xml:lang":"fiu"})
			print("%20s:	*%s" % ("Proto-Form",protoform.text.rstrip().lstrip()))
			#
			match2 = soup2.find('div',class_ = "vergleich")
			for key in codes:
				if (match2.find("span",{"xml:lang":key}) is not None):
					t = match2.find("span",{"xml:lang":key}).text.rstrip().lstrip()
					print("%20s:	%s" % (codes[key],t))
			if(e is not entries[-1]):
				print("\n\n")
