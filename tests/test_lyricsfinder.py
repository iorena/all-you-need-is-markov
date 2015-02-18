from resources import lyricsfinder
import urllib2
import unittest

class LyricsFinderTest(unittest.TestCase):

	def setUp(self):
		self.lyrics = lyricsfinder.LyricsFinder()

	def test_The_Lion_Sleeps_Tonight(self):
		foundLyrics = self.lyrics.getLyrics("The Tokens", "The Lion Sleeps Tonight")
		shouldContain = "In the jungle"
		self.assertTrue(foundLyrics.find(shouldContain))
	
	def test_nonexistant_lyrics(self):
		with self.assertRaises(urllib2.HTTPError):
			self.lyrics.getLyrics("Asdf", "Nonexistant song")
	

	def test_Madonna_Pretender(self):
		foundLyrics = self.lyrics.getLyrics("Madonna", "Pretender")
		shouldContain = "In the jungle"
		self.assertTrue(foundLyrics.find(shouldContain))
	
if __name__ == '__main__':
	unittest.main()
