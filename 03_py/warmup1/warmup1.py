# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  if not(weekday) or vacation:
    return True
  else:
    return False

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


# We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  return a + b

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8


# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
def diff21(n):
  if n >= 21:
    return 2 * (n - 21)
  return 21 - n

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
  if a + b == 10:
    return True
  if a == 10 or b == 10:
    return True;
  return False;

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200-n) <= 10

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False


# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if not negative and a * b < 0:
    return True
  if negative and a < 0 and b < 0:
    return True
  return False

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True



# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def front_back(str):
  if (len(str) > 1):
    new_str = str[-1:] + str[1:len(str) - 1] + str[0:1]
    return new_str
  return str

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'



# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def front3(str):
  return str[:3]*3

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'