print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

#return еще не проходили, но я знаю как она работает
#При вызове функции, можно получить обратно то, что получилось при выполнении функции
#Например вызвав функцию summ, функция summ выполнится и вернет вызывавшему результат назад ( в нашем случае это print)


def summ(number):
  if number < 10:
    return number
  else:
    return number % 10 + summ(number // 10)


def maxx(number):
  max = -1
  while number > 0:
    if number % 10 > max:
      max = number % 10
    number //= 10
  return int(max)


def minn(number):
  min = 10
  while number > 0:
    if number % 10 < min:
      min = number % 10
    number //= 10
  return int(min)


while True:
  #Запрашиваем число у пользователя
  number = int(input("Введите число или 0, чтобы выйти: "))
  #Если число 0, то завершаем работу программы
  if number == 0:
    print("\nРабота программы завершилась!")
    break
  #Запрашиваем действие у пользователя
  action = int(
    input(
      "1 - Сумма цифр числа, \n2 - Максимальная цифра числа, \n3 - Минимальная цифра числа, \n0 - Выход\nВыберите действие: "
    ))
  #Если число 0, то завершаем работу программы
  if action == 0:
    print("\nРабота программы завершилась!")
    break
  #Если число 1, то вызываем функцию подсчета суммы цифр числа
  elif action == 1:
    print("\nСумма цифр числа", number, "равна", summ(number), "\n")
  #Если число 2, то вызываем функцию выявлению максимальной цифры числа
  elif action == 2:
    print("\nМаксимальная цифра числа", number, "равна", maxx(number), "\n")
  #Если число 3, то вызываем функцию выявлению минимальной цифры числа
  elif action == 3:
    print("\nМинимальная цифра числа", number, "равна", minn(number), "\n")
  #Если число НЕ 0, 1, 2, 3, то выводим ошибка ввода
  else:
    print("\nОшибка ввода. Введите 1, 2, 3 или 0 для выхода", "\n")
