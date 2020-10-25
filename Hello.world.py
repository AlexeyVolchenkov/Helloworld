print('Hello world!')
number_1 = int(input('Введите первое число:'))
number_2 = int(input('Введите второе число:'))
function = input('Выберите операцию (+, *, -, /):')
if function == '+':
    print(number_1 + number_2)
elif function == '*':
    print(number_1 * number_2)
elif function == '-':
    print(number_1 - number_2)
elif function == '/':
    print(number_1 / number_2)