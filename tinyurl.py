class Codec:

	def encode(self, longUrl: str) -> str:
		return "http://tinyurl.com/" + longUrl.swapcase()
		

	def decode(self, shortUrl: str) -> str:
		"""Decodes a shortened URL to its original URL.
		"""
		return shortUrl[19:].swapcase()

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyur"
print(codec.decode(codec.encode(url)))