try:
    with open('money.txt', 'r') as file_money:
        money = int(file_money.read())
except (FileNotFoundError, ValueError):
    money = 0


choise = int(input('1: пополнить счет, 2:снять деньги, 3:посмотреть баланс, 4:выйти.:'))
while choise != 4:
    if choise == 1:
        how_much_money = int(input('сколько денег вложить?(только числа)'))
        money += how_much_money
        print('ваш баланс:', money)
        choise = int(input('1: пополнить счет, 2:снять деньги, 3:посмотреть баланс, 4:выйти.:'))
    elif choise == 2:
        how_much_delete = int(input('сколько денег снять?'))
        money -= how_much_delete
        print('ваш баланс:', money)
        choise = int(input('1: пополнить счет, 2:снять деньги, 3:посмотреть баланс, 4:выйти.:'))
    elif choise == 3:
        print('ваш баланс:', money)
        choise = int(input('1: пополнить счет, 2:снять деньги, 3:посмотреть баланс, 4:выйти.:'))
    else:
        print('вы ввели что то не то попробуйте еще раз:')
        choise = int(input('1: пополнить счет, 2:снять деньги, 3:посмотреть баланс, 4:выйти.:'))







with open('money.txt', 'w') as file_money:
    file_money.write(str(money))
