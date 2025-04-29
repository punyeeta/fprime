import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    """Example function: f(x) = x^2"""
    return x**2

def numerical_derivative(func, x, h=0.0001):
    """Compute derivative using central difference method"""
    return (func(x + h) - func(x - h)) / (2 * h)

def plot_function_with_calculus(func, x_min, x_max, num_points=1000):
    """
    Plot a function, its derivative, and its integral
    
    Parameters:
    - func: The function to visualize
    - x_min, x_max: The range for x-axis
    - num_points: Number of points to calculate (affects smoothness)
    """
    # Create x values
    x = np.linspace(x_min, x_max, num_points)
    
    # Compute function values
    y = func(x)
    
    # Compute derivative values
    y_prime = np.array([numerical_derivative(func, xi) for xi in x])
    
    # Compute integral values (starting from the left boundary)
    y_integral = np.zeros_like(x)
    for i in range(1, len(x)):
        # Numerical integration using scipy's quad
        y_integral[i], _ = integrate.quad(func, x_min, x[i])
    
    # Create the plot with a clear figure size
    plt.figure(figsize=(10, 6))
    
    # Plot original function
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    
    # Plot derivative
    plt.plot(x, y_prime, 'r-', linewidth=2, label="f'(x)")
    
    # Plot integral
    plt.plot(x, y_integral, 'g-', linewidth=2, label='∫f(x)dx')
    
    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add reference lines for x=0 and y=0
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Add title and labels
    plt.title('Function with its Derivative and Integral', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    
    # Add legend with clear positioning
    plt.legend(loc='best', fontsize=12)
    
    # Make sure everything fits nicely
    plt.tight_layout()
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Allow for command line arguments to set the range
    import sys
    
    # Default range
    x_min, x_max = -5, 5
    
    # Check if range is provided via command line
    if len(sys.argv) > 2:
        try:
            x_min = float(sys.argv[1])
            x_max = float(sys.argv[2])
        except ValueError:
            print("Invalid range arguments. Using default range.")
    
    # Visualize the function in the specified range
    plot_function_with_calculus(f, x_min, x_max)