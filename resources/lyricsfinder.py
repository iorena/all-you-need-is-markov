import urllib2
from xml.etree.ElementTree import ElementTree

class LyricsFinder:

	def getLyrics(self, artist, song):
		url = 'http://lyrics.wikia.com/' + self.addUnderscore(artist) + ':' + self.addUnderscore(song)
		response = urllib2.urlopen(url)
		tree = ElementTree(file=response)
		root = tree.getroot()
		body = root.find('body')
		for div in body.iter('div'):
			print div.attrib
		#todo: find correct div 	
		#class="WikiaSiteWrapper"
		#return None if wikiasitewrapper[6][1][1]
		lyrics = ""

		return lyrics
		
	def addUnderscore(self, string):
		return string.replace(' ', '_')
