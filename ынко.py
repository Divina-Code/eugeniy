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
   print("*"+___*"*len(word))
   i=0
   toPrint=''
   
   while i < len(word):
        if wopd [i] in letters:
            toPrint=toPrint+word[i]
        else:
            toPrint=toPrint+" _ "
            i =i+1
   print(toPrint)
        


   
   letter=input("введите букву или слово: ")
   
   if len(letter)<1:
      print("Надо ввести букву или слово")

   elif len(letter)==1:
      if letter in word:
         if letter not in letters:
            print("Есть такая буква")
            letters.append(letter)
         else:
            print("Ты уже говорил эту букву")
            lives=lives-1
      else:
         print("&&&&&&&&&&&&&&&&")
         lives=lives-1
          
          

   else:            
      if letter==word:
         print("ТЫ ПОБЕДИЛ game over")
      else:
         print("&&&&&&&&&&&&")
      game=False
         


  

   print("осталось", lives,"жизней")
   print("Угаданные буквы:",letters)
   if lives == 0:
      game = False
