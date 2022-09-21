def sleep_in(weekday, vacation):
  if not(weekday) or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  return a + b

def diff21(n):
  if n >= 21:
    return 2 * (n - 21)
  return 21 - n

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  if a + b == 10:
    return True
  if a == 10 or b == 10:
    return True;
  return False;

def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
  if not negative and a * b < 0:
    return True
  if negative and a < 0 and b < 0:
    return True
  return False

def front_back(str):
  if (len(str) > 1):
    new_str = str[-1:] + str[1:len(str) - 1] + str[0:1]
    return new_str
  return str

def front3(str):
  return str[:3]*3
