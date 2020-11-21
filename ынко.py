from random import randint
words = ["натрий","водород","кислород","уран","азот"]
random_index =randint(0, 4)
word = words[random_index]
print(word)
game=True

lives = 10

while game :
   leter=input("введите букву или слово: ")
   print("*"+"___*"*len(word))
   if leter==word:
      print("ТЫ ПОБЕДИЛ game over")
      game=False


   elif leter in word:
      print ("есть такая буква")

   if leter not in word:
      print("нет")
      lives=lives-1
      print("осталось", lives,"жизней")
   if lives == 0:
      game = False
