def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[:3]*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  ans = ""
  for i in range(0,len(str)):
    ans += str[:i+1]
  return ans

def last2(str):
  ans = 0
  for i in range(0,len(str)-2):
    if str[i:i+2] == str[-2:]:
      ans += 1
  return ans

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
