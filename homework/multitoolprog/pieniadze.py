def pieniadze():

    change = input("Give the amount in USD: ")
    while change.isnumeric() is False:
        change = input("Please provide a number ")
    change1 = int(change)

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
            # instead pf i, try again with next hghest coin value
            coin_num = coin_num + 1
            continue
        elif can_give >= 0:
            # cool, give them that coin!
            result.append(i)
            remainder = round(remainder - i, 1)
            # still more to give
            continue
    print(result)