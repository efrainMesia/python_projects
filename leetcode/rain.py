rainfull_mi = "45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 30.92, 46.8, 67.1, 79.9"
splited_rainfull_mi = rainfull_mi.split(', ')
rainy_days = 0
for rain in splited_rainfull_mi:
    if float(rain)> 75 :
        rainy_days+=1
print(rainy_days)
