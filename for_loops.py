import random 

print("Problem Options: 1,2,3,4,5,6,7,8,9,10")
user = int(input("Which problem would you like to run?: "))

if user == 1: #print out 1 to 1000
 print("running option 1")
 for i in range(1,10001):
   print(i)
elif user == 2: #prints out the odd numbers between 1 and 1000.
  print("running option 2")
  for i in range(1,1001):
    if i % 2 != 0:
        print(i)
elif user == 3: #prints out the numbers between 0 and 1000 that are divisible by 3
  print("running option 3")
  for i in range(0, 1001):
    if i % 3 == 0:
      print(i)
elif user == 4: #prints out the numbers between 1 and 1000 that are divisible by 3 or 5
   print("running option 4")
   for i in range(1, 1001):
     if i % 3 == 0 or i % 5 == 0:
       print(i)
elif user == 5: #asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200, Extra credit if the programs asks again if the number is less than 200
   print("running option 5")
   num=int(input("Enter in a number greater than 200: "))
   for i in range(1, num):
     if i % 11 == 0 and i % 13 == 0:
       print(i)
       num1 = int(input("Enter a number less than 200: "))
       for i in range(1, num):
         if i % 11 == 0 or i % 13 == 0:
           print(i)
elif user == 6: #prints out each letter of a string line by line
  print("running option 6")
  input_string = input("enter a word: ")
  for l in range(len(input_string)):
      line = input_string[l]
      print(line)
elif user == 7: #program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long
  print("running option 7")
  string1 = input("Enter a word (must be 10 letters long): ")
  for l in range(0, len(string1), 2):
    print(string1[l])
elif user == 8: #program that rolls 1000 dice and prints out the number of times each number was rolled
  print("running option 8")
  rolls = [random.randint(1, 6) for _ in range(1000)]
  roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
  for roll in rolls:
    roll_counts[roll] += 1
    print("Results of rolling 1000 dice:")
    for number, count in roll_counts.items():
        print(f"Number {number}: {count} times")  
elif user == 9: #program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not.
  print("running option 9")
  number = int(input("Enter a number: "))
  if number <= 1:
        print(f"{number} is not a prime number.")
  else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
            print(f"{number} is a prime number.")
    else:
            print(f"{number} is not a prime number.")
elif user == 10: #a program that prints out the prime numbers less than 1000
   print("running option 10")
   print("Prime numbers less than 1000:")
   for num in range(2, 1000):
    prime1 = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime1 = 0
            break
    if prime1 == 1:
        print(num)