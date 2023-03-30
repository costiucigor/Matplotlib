import matplotlib.pyplot as plt
print("Values of X:")

x = [1, 2, 3]

y = [2, 4, 1] 
print("Values of Y (thrice of X):")
print(y)
# Plot lines and/or markers to the Axes.
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Draw a line.')
# Display the figure.
plt.show()