#Write a program that continues to prompt for a string (once again, leaving the prompt blank) until the string "quit" is provided. The program should then print the number of "non-quit" strings that were entered.
count = 0
keep_going = True

word = input()
while keep_going:
  count+=1
  print(count)
  word = input()
  if word != 'quit':
    keep_going= True
  else:
    keep_going=False
  print(count)



  