# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  return str*n

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
  return str[:3]*n

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  return str[::2]

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  ans = ""
  for i in range(0,len(str)):
    ans += str[:i+1]
  return ans

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  ans = 0
  for i in range(0,len(str)-2):
    if str[i:i+2] == str[-2:]:
      ans += 1
  return ans

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2


def array_count9(nums):
  ans = 0
  for i in range(0,len(nums)):
    if nums[i] == 9:
      ans += 1
  return ans

def array_front9(nums):
  for i in range(0, min(len(nums),4)):
    if nums[i] == 9:
      return True
  return False

def array123(nums):
  for i in range(0,len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

def string_match(a, b):
  ans = 0
  for i in range(0,min(len(a),len(b))-1):
    if a[i:i+2]==b[i:i+2]:
      ans += 1
  return ans
