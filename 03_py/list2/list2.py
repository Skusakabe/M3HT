def count_evens(nums):
  sum = 0
  for i in nums:
    if i % 2 == 0:
      sum += 1
  return sum
    
def big_diff(nums):
  min = nums[0]
  max = nums[0]
  for i in nums:
    if i > max:
      max = i
    if i < min:
      min = i
  return max - min

def centered_average(nums):
  min = nums[0]
  max = nums[0]
  total = 0
  for i in nums:
    if i > max:
      max = i
    if i < min:
      min = i
    total += i
  return (total - min - max) / (len(nums) - 2)

def sum13(nums):
  sum = 0
  i = 0
  while (i < len(nums)):
    if nums[i] == 13:
      i += 1
    else:
      sum += nums[i]
    i += 1
  return sum

def sum67(nums):
  addMode = True
  sum = 0
  for i in nums:
    if i == 6:
      addMode = False
    if (addMode):
      sum += i
    if i == 7:
      addMode = True
  return sum

def has22(nums):
  for i in range(0,len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
