def is_valid_credit_card_number(number):
  # Check if the number is 16 digits long.
  if len(number) != 16:
    return False

  # Check if the number starts with a 4, 5, 6, or 7.
  if number[0] not in ['4', '5', '6', '7']:
    return False

  # Check if the number is a Luhn number.
  # A Luhn number is a number that passes the following check:
  # 1. The sum of the digits in the even-numbered positions is multiplied by 2.
  # 2. The sum of the digits in the odd-numbered positions is added.
  # 3. The two sums are added together.
  # 4. If the result is divisible by 10, the number is valid.

  even_sum = 0
  odd_sum = 0
  for i in range(1, len(number), 2):
    even_sum += int(number[i])
  for i in range(0, len(number), 2):
    odd_sum += int(number[i])
  total_sum = even_sum + odd_sum
  if total_sum % 10 == 0:
    return True
  else:
    return False
