import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 400)
y = x**2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2')

# Adding title and labels
plt.title('Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')

# Adding grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
