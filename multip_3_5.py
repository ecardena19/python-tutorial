div_3_5 = 0
raw_data = list(range(1, 100))

for e in raw_data:
    if e % 3 == 0 and e % 5 == 0:
        div_3_5 += e
        print(div_3_5)
