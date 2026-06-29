import numpy as np

temp_array_C = np.random.randint(-10, 46, size=(364,1))

temp_array_f = (temp_array_C * 9 / 5) + 32


print(temp_array_f)

# Hottest Day
max_temp = np.max(temp_array_f)
max_day = np.argmax(temp_array_f)


# Coldest Day
min_temp = np.min(temp_array_f)
min_day = np.argmin(temp_array_f)


print(f"Hottest Day: Day {max_day}, Temp: {max_temp}°F")
print(f"Coldest Day: Day {min_day}, Temp: {min_temp}°F")

# Weekly Average

# Reshape into weeks (52weeks, 7days each)
weekly_temps = temp_array_f.reshape((52, 7))

# Calculate mean temp for each week
weekly_avg = np.mean(weekly_temps, axis=1)

print("Weelly Averages:")
print(weekly_avg)


# Hottest and coldest week
hottest_week = np.argmax(weekly_avg)
coldest_week = np.argmin(weekly_avg)

print(f"\nHottest week: Week {hottest_week}, Avg: {weekly_avg[hottest_week]:.2f}°F")
print(f"Coldest week: Week {coldest_week}, Avg: {weekly_avg[coldest_week]:.2f}°F")

# Seve to file
np.savetxt('temprature_data.csv', temp_array_f, delimiter=',', fmt='%2f', header='Temprature (Fahrenheit)')