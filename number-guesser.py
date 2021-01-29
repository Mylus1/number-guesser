from random import randint


number = randint(0, 100)

while True:
  try:
    user_number = int(input("Enter a number: "))
  except:
    print("that's not a number!")
    continue

  if user_number > number:
    print("The number is lower")

  if user_number < number:
    print("The number is higher")

  if user_number == number:
    print("You've got it right!")
    break

