import unittest, twoSum

class TestTwoSum(unittest.TestCase):
  def setUp(self):
    self.solution = twoSum.Solution
  def test_Passing1(self):
    self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])

  def test_Passing2(self):
    self.assertEqual(self.solution.twoSum([3,2,4], 6),[1,2])

  def test_Passing3(self):
    self.assertEqual(self.solution.twoSum([3,3], 6), [0,1])

  def test_Failing1(self):
    self.assertNotEqual(self.solution.twoSum([2,3,3], 6), [0,1])

if __name__ == "__main__":
  unittest.main
