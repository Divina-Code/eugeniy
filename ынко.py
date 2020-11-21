from random import randint

word="натрий"
score=10
game=True

while game :
   leter=input("введите букву или слово: ")

   if leter==word:
      print("ТЫ ПОБЕДИЛ game over")
      game=False


   elif leter in word:
      print ("есть такая буква")

   if leter not in word:
      print("нет")
      score=score-1
