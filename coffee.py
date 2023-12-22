prise_per_coffee = 50
total_inserted = 0
print("Нужная сумма:",prise_per_coffee - total_inserted)

while total_inserted < prise_per_coffee:
    coin = input("Вставьте монету:")

    if coin == "50" or coin == "20" or coin == "10" or coin == "5":
        total_inserted += int(coin)
        print(f"Ваша сдача: {prise_per_coffee - total_inserted}")
    else:
        print("Нужная сумма: ",prise_per_coffee - total_inserted)

change_owed = total_inserted - prise_per_coffee

print(f"Ваша сдача: {change_owed}")