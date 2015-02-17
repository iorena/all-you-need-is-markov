from resources import parsebillboard 
import unittest

class BillboardParserTest(unittest.TestCase):
	
	def setUp(self):
		self.parser = parsebillboard.BillboardParser()
		self.songlist1961 = self.parser.getSongList(1961)

	def test_1961_list_length(self):
		self.assertEqual(len(self.songlist1961), 23)

	def test_1961_list_contains_Elvis(self):
		self.assertEqual(self.songlist1961[0][1], "Elvis Presley")

if __name__ == '__main__':
	unittest.main()
