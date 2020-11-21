Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randit
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from random import randit
ImportError: cannot import name 'randit' from 'random' (C:\Users\SLBar\AppData\Local\Programs\Python\Python39\lib\random.py)
>>> word="австралия"
>>> leter=input("введите букву: ")
введите букву: 
>>> if leter in word
SyntaxError: invalid syntax
>>>    print ("есть такая буква")
   
SyntaxError: unexpected indent
>>> if leter not in the word
SyntaxError: invalid syntax
>>>    print("нет такой буквы")