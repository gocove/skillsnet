class Solution(object):
  def numberOfSubstrings(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

def main():
  s, k = "abacb", 2
  print("s=", s, "k=", k)
  s = Solution().numberOfSubstrings(s, k)
  print(s)
  
if __name__ == '__main__':
  main()
