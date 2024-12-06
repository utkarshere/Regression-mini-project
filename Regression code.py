import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the data from the CSV file
data = pd.read_csv("height.csv")

#Assigning time and height values to variables
time_points = data['Time (s)'].values
height_points_noisy = data['Height (m)'].values

#Performing quadratic equation to find coefficients

coefficients = np.polyfit(time_points, height_points_noisy, 2) #degree 2
a, b, c = coefficients


#Calculating the acceleration g from coefficient a
g_calculated = -2*a #since a = -1/2*g from comparing the height and time equation to quadratic equation


#Generating fitted quadratic curve for visualization
t_fit = np.linspace(0,10,100)
h_fit = a * t_fit**2 + b * t_fit + c


#Plotting the fitted curve and their original noisy data
plt.figure(figsize=(10, 6))
plt.scatter(time_points, height_points_noisy, color = 'blue', label = 'Noisy Data Points')
plt.plot(t_fit, h_fit, color = 'red', label = 'Fitted Quadratic Curve')
plt.title("Quadratic Regression: Height vs Time")
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.grid(True)
plt.show()

#Displaying calculated g
print(g_calculated)
