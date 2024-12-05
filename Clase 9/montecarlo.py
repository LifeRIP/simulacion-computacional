import numpy as np
import matplotlib.pyplot as plt

# limits of integration
a = 0
b = 1
N = 1000

# function to calculate the sin of a particular 
# value of x
def f(x):
    return x - x**2

# list to store all the values for plotting 
plt_vals = []

# we iterate through all the values to generate 
# multiple results and show whose intensity is 
# the most.
for _ in range(N):
    
    # array of zeros of length N
    ar = np.zeros(N)
    
    # iterating over each Value of ar and filling it
    # with a random value between the limits a and b
    for i in range(len(ar)):
        ar[i] = np.random.uniform(a, b)

    
    # variable to store sum of the functions of different
    # values of x
    integral = 0.0
    
    # iterates and sums up values of different functions 
    # of x
    for i in ar:
        integral += f(i)
    
    # we get the answer by the formula derived above
    ans = (b - a) / float(N) * integral
    
    # appends the solution to a list for plotting the graph
    plt_vals.append(ans)

# Calculate the mean of the areas
mean_area = np.mean(plt_vals)

# Plotting the function f(x)
x = np.linspace(a, b, 1000)
y = f(x)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y, label='f(x) = x - x^2')
plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.title('Function f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.text(0.5, 0.5, f'Area = {mean_area:.4f}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Plotting the histogram of the areas calculated
plt.subplot(1, 2, 2)
plt.hist(plt_vals, bins=30, ec='black')
plt.title('Distributions of areas calculated')
plt.xlabel('Areas')

plt.tight_layout()
plt.show()