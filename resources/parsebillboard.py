import urllib2
from xml.etree.ElementTree import ElementTree

class BillboardParser:

	def parseBillboard(self):
		years = range(1960, 2014) 
		listlist = []
		for year in years:
			songlist = getSongList(years)
			listlist.append(songlist)

	def getSongList(self, year):
		songlist = []
		response = urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_' + str(year))

		tree = ElementTree(file=response)
		root = tree.getroot()
		root = root.find('body')
		for child in root[2][4][3][2]:
			if len(list(child)) < 4:
				continue
			if len(list(child[1])) == 0:
				continue
			if len(list(child[2])) == 0:
				continue
			artist = child[2][0].attrib['title']
			song = child[1][0].attrib['title']
			songlist.append((song, artist))

		return songlist
