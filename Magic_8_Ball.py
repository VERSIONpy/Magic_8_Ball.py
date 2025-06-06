import random 
Question = input("Enter ur Question: ")

num = random.randint(1, 9)


if num == 1:
  print("Yes - definitely.")
elif num == 2:
  print("Very doubtful.")
elif num == 3:
  print("Outlook not so good.")
elif num == 4:
  print("My sources say no.")
elif num == 5:
  print("Better not tell you now.")
elif num == 6:
  print("Ask again later.")
elif num == 7:
  print("Reply hazy, try again.")
elif num == 8:
  print("Without a doubt.")
else:
  print("It is decidedly so.")