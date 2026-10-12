# Dispersion: Variance & Std. Deviation

data = [4, 8, 6, 10, 12]

mean_of_data = sum(data) / len(data)  # Where is the center

variance = sum((x - mean_of_data) ** 2 for x in data) / len(
    data
)  # How much is the data spread out

std_dev = variance**0.5  # How far from the mean is a typical value

print(mean_of_data)
print(variance)
print(std_dev)

from statistics import mean, pvariance, pstdev

print(mean(data))
print(pvariance(data))
print(pstdev(data))

cv = (std_dev / mean_of_data) * 100
print(cv)

value = 11
z_score = (value - mean_of_data) / std_dev
print(z_score)
