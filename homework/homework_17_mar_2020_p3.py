#Zadanie 3

change = input("Give the amount in USD: ")
change1 = float(change)

# subtrct highest coinn value from change, then...
# if change is more than 0, we can give them that coin, AND there's still more to give
# if change is less than 0, we gave too much... so don't give them that coin
# if change is exactly 0, we're done!
coins = [5, 2, 1, 0.5, 0.2, 0.1]
coin_num = 0
result = []

remainder = change1

while remainder > 0:
    i = coins[coin_num]
    can_give = round(remainder - i, 1)
    print(f"can we give them {i} if they have {remainder} left to receive?")

    if can_give < 0:
        # gave them too much
        #instead pf i, try again with next hghest coin value
        coin_num = coin_num + 1
        continue
    elif can_give >= 0:
        # cool, give them that coin!
        result.append(i)
        remainder = round(remainder - i, 1)
        # still more to give
        continue

print(result)




