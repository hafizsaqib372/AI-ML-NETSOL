# Central Tendancy

from statistics import mean, median, mode, multimode

prices = [10, 15, 12, 14, 9, 60, 13, 12, 15, 9]

print(mean(prices))  # avarage
print(median(prices))  # central value
print(mode(prices))  # most frequent value
print(multimode(prices))
print(sorted(prices))
print(prices)
prices.sort()
print(prices)
