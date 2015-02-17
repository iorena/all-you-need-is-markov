import urllib2
from xml.etree.ElementTree import ElementTree

class LyricsFinder:

	def getLyrics(self, artist, song):
		response = urllib2.urlopen('http://lyrics.wikia.com/' + artist + ':' + song)
		tree = ElementTree(file=response)
		root = tree.getRoot()
		body = root.find('body')
		#todo: find correct div 	
		lyrics = ""

		return lyrics
		
