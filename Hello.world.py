print('Hello world!')
number_1 = int(input('Введите первое число:'))
number_2 = int(input('Введите второе число:'))
function = input('Выберите операцию (+, *, -, /):')
number_3 = int(input('Введите число, которое должно получиться:'))
if function == '+':
    sum1 = number_1 + number_2
    print('Результат сложения:',sum1)
    if sum1 == number_3:
        print('Функция сложения для чисел', number_1, 'и', number_2, 'вернула', sum1, '- результат верный')
    elif sum1 != number_3:
        print('Функция сложения для чисел', number_1, 'и', number_2, 'вернула', sum1, '- результат неверный')
elif function == '*':
    multi = number_1 * number_2
    print('Результат умножения:',multi)
    if multi == number_3:
        print('Функция умножения для чисел', number_1, 'и', number_2, 'вернула', multi, '- результат верный')
    elif multi != number_3:
        print('Функция умножения для чисел', number_1, 'и', number_2, 'вернула', multi, '- результат неверный')
elif function == '-':
    sub = number_1 - number_2
    print('Результат вычитания:',sub)
    if sub == number_3:
        print('Функция вычитания для чисел', number_1, 'и', number_2, 'вернула', sub, '- результат верный')
    elif sub != number_3:
        print('Функция вычитания для чисел', number_1, 'и', number_2, 'вернула', sub, '- результат неверный')
elif function == '/':
    if number_2 == 0:
        print('На 0 делить нельзя')
    else:
        div = number_1 / number_2
        print('Результат деления первого числа на второе:', div)
        if div == number_3:
            print('Функция деления для чисел', number_1, 'и', number_2, 'вернула', div, '- результат верный')
        elif div != number_3:
            print('Функция деления для чисел', number_1, 'и', number_2, 'вернула', div, '- результат неверный')
else:
    print('Выбарана неправильная операция')