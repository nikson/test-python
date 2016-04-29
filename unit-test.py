import unittest;


class test(unittest.TestCase):
	
	def test_one(self):
		self.assertTrue(True);

	@unittest.skip('just skip this test')
	def test_two(self):
		self.assertTrue(True);

if __name__ == '__main__':
	unittest.main()
