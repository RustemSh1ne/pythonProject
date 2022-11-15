
try:
    tickets_number = int(input('Введите количество билетов:'))
    if tickets_number <= 0:
        raise ValueError('Количество билетов может быть только больше нуля!')
except ValueError as error:
    print(error, 'Количество билетов может быть только число и только целое!')
else:

     current_age = 0    #возраст текущего участника
     age = []           #список, возраст каждого участника
     cost = []          #список, стоимость каждого билета
     total_cost = 0     #полная стоимость без скидки

     for i in range(0,tickets_number):
         print()
         print('Участник', i + 1)


         try:
             current_age = int(input('Введите возраст участника:'))
             if current_age > 100 or current_age <= 0:
                 raise ValueError('Участнику не может быть столько лет')
         except ValueError as error:
             print(error)
             print('Неправильный возраст')
             break
         else:

             age.append(current_age)
             if current_age < 18:
                 cost.append(0)
                 print('Возраст менее 18 лет, стоимость    0')

             elif current_age < 25:
                 cost.append(990)
                 print('Возраст от 18 до 25 лет, стоимость  990')

             elif current_age <= 100:
                 cost.append(1390)
                 print('Возраст от 25 лет, стоимость 1390')


     if tickets_number == len(cost):  #у всех участников правильный возраст
         total_cost = sum(cost)
         print()
         print('Полная стоимость заказа')

         if tickets_number > 3:
             print('со скидкой 10% за регистрацию больше трёх человек', int(total_cost * 0.9))
         else:
             print(total_cost)


