import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    """Example function: f(x) = x^2"""
    return x**3 - 3*x

def numerical_derivative(func, x, h=0.0001):
    """Compute derivative using central difference method"""
    return (func(x + h) - func(x - h)) / (2 * h)

def plot_function_with_separated_calculus(func, x_min, x_max, num_points=1000):
    """
    Plot a function, its derivative, and its integral in side-by-side subplots
    
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
    
    # Create a figure with 3 side-by-side subplots
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    # Plot 1: Original function
    axs[0].plot(x, y, 'b-', linewidth=2)
    axs[0].set_title('Original Function', fontsize=12)
    axs[0].grid(True, linestyle='--', alpha=0.7)
    axs[0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axs[0].axvline(x=0, color='k', linestyle='-', alpha=0.3)
    axs[0].set_xlabel('x', fontsize=12)
    axs[0].set_ylabel('f(x)', fontsize=12)
    
    # Plot 2: Derivative
    axs[1].plot(x, y_prime, 'r-', linewidth=2)
    axs[1].set_title('First Derivative', fontsize=12)
    axs[1].grid(True, linestyle='--', alpha=0.7)
    axs[1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axs[1].axvline(x=0, color='k', linestyle='-', alpha=0.3)
    axs[1].set_xlabel('x', fontsize=12)
    axs[1].set_ylabel('f\'(x)', fontsize=12)
    
    # Plot 3: Integral
    axs[2].plot(x, y_integral, 'g-', linewidth=2)
    axs[2].set_title('Integral', fontsize=12)
    axs[2].grid(True, linestyle='--', alpha=0.7)
    axs[2].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axs[2].axvline(x=0, color='k', linestyle='-', alpha=0.3)
    axs[2].set_xlabel('x', fontsize=12)
    axs[2].set_ylabel('∫f(x)dx', fontsize=12)
    
    # Add an overall title
    fig.suptitle('Function Calculus Visualization', fontsize=16)
    
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
    plot_function_with_separated_calculus(f, x_min, x_max)