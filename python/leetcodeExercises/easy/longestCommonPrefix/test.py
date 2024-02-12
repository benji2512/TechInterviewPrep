# "TODO" Write tests for thise
# "BODY" Use pytest to write a passing and failing test for this

class TestTwoSum(unittest.TestCase):
  def setUp(self):
    self.solution = twoSum.Solution
  def test_Passing1(self):
    self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])

if __name__ == "__main__":
  unittest.main
