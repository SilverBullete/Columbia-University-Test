from decimal import Decimal
amount = input('Change amount?')
amount = Decimal(amount)
money = [20, 10, 5, 1, Decimal('0.25'),
         Decimal('0.1'), Decimal('0.05'), Decimal('0.01')]
li = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 8):
    li[i] = str(int(amount/money[i]))
    amount = amount % money[i]
print('The bills or the change should be: ')
print(li[0]+' twenties')
print(li[1]+' tens')
print(li[2]+' fives')
print(li[3]+' ones')
print(li[4]+' quarters')
print(li[5]+' dimes')
print(li[6]+' nickels')
print(li[7]+' pennies')
