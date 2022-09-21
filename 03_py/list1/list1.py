def first_last6(nums):
  return nums[-1] == 6 or nums[0] == 6

def common_end(a, b):
  return a[-1] == b[-1] or a[0] 

def make_pi():
  return [3, 1, 4]

def reverse3(nums):
  return nums[-1::-1]

def middle_way(a, b):
  return [a[1], b[1]]

def rotate_left3(nums):
  lst = nums[1:]
  lst.append(nums[0])
  return lst

def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3
