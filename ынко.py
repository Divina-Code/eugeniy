from random import randint

word="натрий"

game=True

lives = 10

while game :
   leter=input("введите букву или слово: ")

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
