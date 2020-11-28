from random import randint
words = ["натрий","водород","кислород","уран","азот"]
random_index =randint(0, 4)
word = words[random_index]
print(word)
game=True

lives = 10

letters=[]
while game :
   print ()
   print()
   print("*"+"___*"*len(word))
   leter=input("введите букву или слово: ")
   if len(letter)<1
      print("Надо ввести букву или слово")

      elif len(letter)==1
         if letter==word:
            if letter not in letters:
             print("Есть такая буква")
             letters.append(letter)
          else:
              print("Ты уже говорил эту букву")
              lives=lives-1
   if leter==word:
      print("ТЫ ПОБЕДИЛ game over")
      game=False


   elif leter in word:
      print ("есть такая буква")
      letters.append(letter)
   if leter not in word:
      print("нет")
      lives=lives-1
   print("осталось", lives,"жизней")
   print("Угаданные буквы:",letters)
   if lives == 0:
      game = False
