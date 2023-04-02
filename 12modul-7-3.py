money = int(input("Введите сумму:"))
deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for c in list(per_cent.values()):
    deposit.append(int((money * c) / 100))
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))