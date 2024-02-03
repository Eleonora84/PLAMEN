bitcoins = int(input())
yuans = float(input())
commission = float(input()) /100

bitcoins_to_leva = bitcoins * 1168
yuans_to_dollars = yuans * 0.15
dollars_to_leva = yuans_to_dollars * 1.76
sum_leva = bitcoins_to_leva + dollars_to_leva
sum_euro = sum_leva / 1.95

sum_euro -= commission * sum_euro

print(round(sum_euro,2))