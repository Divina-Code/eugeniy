from random import randint




print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))
print()


players = []
for i in range(n):
    name = input("Введите имя " +str(i+1)+"-го игрока:\t" )
    players.append(name)

print("\nИГРОКИ: ", players)

points = []
for j in range(n):
    random_points = randint(1, 10)
    points.append(random_points)
    print(players[j], "Ваш счёт:", random_points)

print("\nОЧКИ: ",points)
playORnot=[]
for n in range
while playORnot.count:(True)
    print("\n \t\tROUHD")
    for a in range(n):
        if playORnot[n] == True
        answer = input(players[a] + ' будете брать карту? [ДА\НЕТ]')

        answer = answer.upper()
        answer = answer.strip()

        if answer == "ДА":
            print("Вы ответили ", answer)
            random_points = randint(1, 10)
            points[n]+=random_points
            print(players[n], "Вам выпало:", random_points)
            if points [n] >=21
                playORnot=Fals
        elif answer == "НЕТ":
            print("Вы ответили ", answer)
            playORnot[n]=Fals
        else:
            print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")

