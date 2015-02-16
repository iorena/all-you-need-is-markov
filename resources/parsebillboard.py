import urllib2
from xml.etree.ElementTree import ElementTree

years = range(1960, 2014) 

listlist = []

for year in years:
	songlist = []
	
	response = urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_' + str(year))

	tree = ElementTree(file=response)
	root = tree.getroot()
	root = root.find('body')
	for child in root[2][4][3][2]:
		for tr in child:
			song = tr.find('a')
			if song is not None:
				songlist.append(song.attrib.get('title'))	#todo: parse artist and song name
				print song.attrib.get('title')
	listlist.append(songlist)
