from resources import lyricsfinder
import unittest

class LyricsFinderTest(unittest.TestCase):

	def setUp(self):
		self.lyrics = lyricsfinder.LyricsFinder()

	def test_The_Lion_Sleeps_Tonight(self):
		foundLyrics = self.lyrics.getLyrics("The Tokens", "The Lion Sleeps Tonight")
		shouldContain = "In the jungle"
		self.assertTrue(foundLyrics.find(shouldContain))
	
if __name__ == '__main__':
	unittest.main()
